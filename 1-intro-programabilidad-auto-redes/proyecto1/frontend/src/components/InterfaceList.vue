<template>
  <div>
    <h1>Interfaces</h1>
    <ul v-if="interfaces">
      <li v-for="network_interface in interfaces" :key="network_interface.name">
        {{ network_interface.if_name }} - {{ network_interface.ip_address }}
      </li>
    </ul>
    <div v-else-if="isLoading">Loading...</div>
    <div v-else-if="error">{{ error }}</div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import api from '../services/api';

const interfaces = ref(null);
const isLoading = ref(false);
const error = ref(null);

const fetchInterfaces = async () => {
  isLoading.value = true;
  try {
    const response = await api.getInterfaces();
    interfaces.value = response.data;
  } catch (err) {
    error.value = 'Error fetching interfaces';
  } finally {
    isLoading.value = false;
  }
};

fetchInterfaces();
</script>
