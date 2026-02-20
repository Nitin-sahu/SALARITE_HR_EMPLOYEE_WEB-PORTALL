import axios from "axios";

const API = axios.create({ baseURL: "http://localhost:8000" });

export const getTasks = () => API.get("/tasks");
export const createTask = (data) => API.post("/tasks", data);
export const updateTask = (id, status) => API.put(`/tasks/${id}`, { status });

export const getInterviews = () => API.get("/interviews");
export const createInterview = (data) => API.post("/interviews", data);

export const getActivity = () => API.get("/activity");