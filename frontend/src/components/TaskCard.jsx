import React from "react";
function TaskCard({ task, onEdit, onDelete }) {
  const statusLabel = task.status.replace('_', ' ');

  return (
    <article className="task-card">
      <div className="task-card-header">
        <div>
          <h3>{task.title}</h3>
        </div>
        <div className="task-meta">
          <span className={`status-badge status-${task.status.toLowerCase()}`}>{statusLabel}</span>
          <span className={`priority-badge priority-${task.priority.toLowerCase()}`}>{task.priority}</span>
        </div>
      </div>

      <p className="task-description">{task.description || 'No description provided.'}</p>

      <div className="task-card-footer">
        <small>
          Updated {new Date(task.updated_at).toLocaleString()}
        </small>
        <div className="task-actions">
          <button type="button" className="secondary-button" onClick={() => onEdit(task)}>
            Edit
          </button>
          <button type="button" className="danger-button" onClick={() => onDelete(task.id)}>
            Delete
          </button>
        </div>
      </div>
    </article>
  );
}

export default TaskCard;
