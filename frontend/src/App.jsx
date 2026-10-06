import React from "react";
import { useEffect, useMemo, useState } from 'react';
import TaskCard from './components/TaskCard';
import TaskForm from './components/TaskForm';
import { taskApi } from './services/taskApi';
import './App.css';

const defaultForm = {
  title: '',
  description: '',
  status: 'PENDING',
  priority: 'MEDIUM',
};

function App() {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [formError, setFormError] = useState('');
  const [showForm, setShowForm] = useState(false);
  const [isEditing, setIsEditing] = useState(false);
  const [currentTaskId, setCurrentTaskId] = useState(null);
  const [searchTerm, setSearchTerm] = useState('');
  const [statusFilter, setStatusFilter] = useState('ALL');
  const [priorityFilter, setPriorityFilter] = useState('ALL');
  const [formData, setFormData] = useState(defaultForm);

  const loadTasks = async () => {
    try {
      setLoading(true);
      setError('');
      const response = await taskApi.fetchTasks(searchTerm, statusFilter, priorityFilter);
      setTasks(response);
    } catch (fetchError) {
      setError(fetchError.message || 'Unable to load tasks. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadTasks();
  }, [searchTerm, statusFilter, priorityFilter]);

  const totalTasks = useMemo(() => tasks.length, [tasks]);

  const handleFormSubmit = async (event) => {
    event.preventDefault();

    const trimmedTitle = formData.title.trim();
    if (!trimmedTitle) {
      setFormError('Please enter a task title.');
      return;
    }

    if (trimmedTitle.length > 150) {
      setFormError('Title must be 150 characters or less.');
      return;
    }

    try {
      setFormError('');
      const payload = {
        ...formData,
        title: trimmedTitle,
        description: formData.description.trim() || null,
      };

      if (isEditing && currentTaskId) {
        await taskApi.updateTask(currentTaskId, payload);
      } else {
        await taskApi.createTask(payload);
      }

      setFormData(defaultForm);
      setShowForm(false);
      setIsEditing(false);
      setCurrentTaskId(null);
      await loadTasks();
    } catch (submitError) {
      setFormError(submitError.message || 'Unable to save task. Please try again.');
    }
  };

  const startCreateMode = () => {
    setShowForm(true);
    setIsEditing(false);
    setCurrentTaskId(null);
    setFormData(defaultForm);
    setFormError('');
  };

  const startEditMode = (task) => {
    setShowForm(true);
    setIsEditing(true);
    setCurrentTaskId(task.id);
    setFormData({
      title: task.title,
      description: task.description || '',
      status: task.status,
      priority: task.priority,
    });
    setFormError('');
  };

  const handleDeleteTask = async (taskId) => {
    const confirmed = window.confirm('Are you sure you want to delete this task?');
    if (!confirmed) {
      return;
    }

    try {
      await taskApi.deleteTask(taskId);
      await loadTasks();
    } catch (deleteError) {
      setError(deleteError.message || 'Unable to delete task. Please try again.');
    }
  };

  return (
    <main className="app-shell">
      <div className="page-header">
        <div>
          <p className="eyebrow">Task dashboard</p>
          <h1>Task Management</h1>
        </div>
        <button type="button" className="primary-button" onClick={startCreateMode}>
          + Add Task
        </button>
      </div>

      <section className="toolbar">
        <input
          type="search"
          value={searchTerm}
          onChange={(event) => setSearchTerm(event.target.value)}
          placeholder="Search tasks..."
          aria-label="Search tasks"
        />

        <select value={statusFilter} onChange={(event) => setStatusFilter(event.target.value)} aria-label="Filter by status">
          <option value="ALL">Status: All</option>
          <option value="PENDING">Pending</option>
          <option value="IN_PROGRESS">In Progress</option>
          <option value="COMPLETED">Completed</option>
        </select>

        <select value={priorityFilter} onChange={(event) => setPriorityFilter(event.target.value)} aria-label="Filter by priority">
          <option value="ALL">Priority: All</option>
          <option value="LOW">Low</option>
          <option value="MEDIUM">Medium</option>
          <option value="HIGH">High</option>
        </select>
      </section>

      {showForm && (
        <TaskForm
          formData={formData}
          onChange={setFormData}
          onSubmit={handleFormSubmit}
          onCancel={() => {
            setShowForm(false);
            setFormData(defaultForm);
            setFormError('');
            setIsEditing(false);
            setCurrentTaskId(null);
          }}
          isEditing={isEditing}
          error={formError}
        />
      )}

      {error && <div className="banner banner-error">{error}</div>}

      {loading ? (
        <div className="state-box">Loading tasks...</div>
      ) : tasks.length === 0 ? (
        <div className="state-box empty-state">
          <h3>No tasks found</h3>
          <p>Try a different search or create your first task.</p>
        </div>
      ) : (
        <>
          <div className="summary-row">
            <span>{totalTasks} task{totalTasks === 1 ? '' : 's'}</span>
          </div>

          <section className="task-list">
            {tasks.map((task) => (
              <TaskCard key={task.id} task={task} onEdit={startEditMode} onDelete={handleDeleteTask} />
            ))}
          </section>
        </>
      )}
    </main>
  );
}

export default App;
