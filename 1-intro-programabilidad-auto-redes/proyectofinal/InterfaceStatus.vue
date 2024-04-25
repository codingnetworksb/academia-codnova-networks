<template>
  <div class="interface-status">
    <h1>Estado de las interfaces - {{ routerIp }} </h1> 
    <button @click="fetchInterfaceStatus">Actualizar</button>

    <div v-if="isLoading" class="loading-message">
      Cargando...
    </div>

    <div v-else-if="error" class="error-message">
      Error al cargar los datos: {{ error }}
    </div>

    <ul v-else class="interface-list">
      <li v-for="interface in interfaces" :key="interface.name">
        <div class="interface-name"> {{ interface.name }}</div>
        <div class="interface-status" 
                :class="'status-' + interface.status.toLowerCase()">
            {{ interface.status }}
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import axios from 'axios';

export default {
  props: {
    routerIp: {
      type: String,
      required: true,
    },
  },
  setup() {
    const interfaces = ref([]);
    const isLoading = ref(false);
    const error = ref(null);

    const fetchInterfaceStatus = async () => {
      error.value = null;  
      isLoading.value = true;
      try {
        const response = await axios.get(
          `http://backend-api:8000/estado-interfaces?router_ip=${routerIp}` 
        );
        interfaces.value = response.data["ietf-interfaces:interfaces"]["interface"]; 
      } catch (error) {
        error.value = error.message;
      } finally {
        isLoading.value = false;
      }
    };

    onMounted(fetchInterfaceStatus);

    return { interfaces, isLoading, error, fetchInterfaceStatus };
  },
};
</script>

<style>
/* Los estilos permanecen igual */
</style>
