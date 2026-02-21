import axios from "axios";

const baseURL = `${import.meta.env.VITE_APP_API_BASE_URL}`;

const ProxyClient = axios.create({
    baseURL,
});
export default ProxyClient;
