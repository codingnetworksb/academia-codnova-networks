import axios from 'axios';

const apiClient = axios.create({
    baseURL: 'http://backend:8000' // Update with backend URL
});

export default {
    getInterfaces() {
        return apiClient.get('/interfaces');
    }
    // ...Other API methods
};
