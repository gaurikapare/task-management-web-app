const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

async function request(path, options = {}) {
  const response = await fetch(`${API_URL}${path}`, {
    headers: {
      'Content-Type': 'application/json',
      ...(options.headers || {}),
    },
    ...options,
  });

  let payload = null;
  try {
    payload = await response.json();
  } catch (error) {
    payload = null;
  }

  if (!response.ok) {
    const message = payload?.detail || payload?.message || 'Request failed.';
    throw new Error(message);
  }

  return payload;
}

export const taskApi = {
  fetchTasks(search = '', status = 'ALL', priority = 'ALL') {
    const params = new URLSearchParams();

    if (search) {
      params.set('search', search);
    }

    if (status && status !== 'ALL') {
      params.set('status', status);
    }

    if (priority && priority !== 'ALL') {
      params.set('priority', priority);
    }

    const query = params.toString();
    return request(`/api/tasks${query ? `?${query}` : ''}`);
  },

  getTask(taskId) {
    return request(`/api/tasks/${taskId}`);
  },

  createTask(taskData) {
    return request('/api/tasks', {
      method: 'POST',
      body: JSON.stringify(taskData),
    });
  },

  updateTask(taskId, taskData) {
    return request(`/api/tasks/${taskId}`, {
      method: 'PUT',
      body: JSON.stringify(taskData),
    });
  },

  deleteTask(taskId) {
    return request(`/api/tasks/${taskId}`, {
      method: 'DELETE',
    });
  },
};
