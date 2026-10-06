import React from "react";
function TaskForm({ formData, onChange, onSubmit, onCancel, isEditing, error }) {
  const handleInputChange = (event) => {
    const { name, value } = event.target;
    onChange({ ...formData, [name]: value });
  };

  return (
    <form className="task-form" onSubmit={onSubmit}>
      <div className="form-header">
        <h2>{isEditing ? 'Edit task' : 'Add a new task'}</h2>
      </div>

      {error && <div className="form-error">{error}</div>}

      <div className="field-group">
        <label htmlFor="title">Title</label>
        <input
          id="title"
          name="title"
          value={formData.title}
          onChange={handleInputChange}
          placeholder="Enter task title"
          maxLength={150}
        />
      </div>

      <div className="field-group">
        <label htmlFor="description">Description</label>
        <textarea
          id="description"
          name="description"
          value={formData.description}
          onChange={handleInputChange}
          placeholder="Add details"
          rows="4"
        />
      </div>

      <div className="field-row">
        <div className="field-group">
          <label htmlFor="status">Status</label>
          <select id="status" name="status" value={formData.status} onChange={handleInputChange}>
            <option value="PENDING">Pending</option>
            <option value="IN_PROGRESS">In Progress</option>
            <option value="COMPLETED">Completed</option>
          </select>
        </div>

        <div className="field-group">
          <label htmlFor="priority">Priority</label>
          <select id="priority" name="priority" value={formData.priority} onChange={handleInputChange}>
            <option value="LOW">Low</option>
            <option value="MEDIUM">Medium</option>
            <option value="HIGH">High</option>
          </select>
        </div>
      </div>

      <div className="action-row">
        <button type="submit" className="primary-button">
          {isEditing ? 'Save changes' : 'Create task'}
        </button>
        {isEditing && (
          <button type="button" className="secondary-button" onClick={onCancel}>
            Cancel
          </button>
        )}
      </div>
    </form>
  );
}

export default TaskForm;
