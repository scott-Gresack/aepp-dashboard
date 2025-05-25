<template>
  <div class="p-6 space-y-6">
    <h1 class="text-2xl font-bold">AEPP Use Case Dashboard</h1>

    <!-- Web Analytics -->
    <section>
      <h2 class="text-xl font-semibold">Web Analytics (Explore 201)</h2>
      <div class="grid gap-4 md:grid-cols-2">
        <div>
          <button @click="fetchEventCount" class="btn">Count Events</button>
          <p v-if="eventCount !== null">Total Events: {{ eventCount }}</p>
        </div>
        <div>
          <button @click="fetchVisitors" class="btn">Unique Visitors</button>
          <p v-if="uniqueVisitors !== null">Unique Visitors: {{ uniqueVisitors }}</p>
        </div>
        <div>
          <button @click="fetchSessions" class="btn">Session Counts</button>
          <p v-if="sessions !== null">Sessions: {{ sessions }}</p>
        </div>
        <div>
          <button @click="fetchPopularPages" class="btn">Popular Pages</button>
          <ul v-if="popularPages.length">
            <li v-for="(page, index) in popularPages" :key="index">{{ page }}</li>
          </ul>
        </div>
      </div>
    </section>

    <!-- AEPP APIs -->
    <section>
      <h2 class="text-xl font-semibold">AEPP Monitoring</h2>
      <div class="space-y-4">
        <button class="btn" @click="triggerAgentCheck">Run Monitoring Check</button>
        <ul v-if="agentLogs.length" class="text-sm bg-gray-100 p-4 rounded">
          <li v-for="(log, index) in agentLogs" :key="index" class="mb-1">{{ log }}</li>
        </ul>
      </div>
    </section>

    <!-- Visualization -->
    <section>
      <h2 class="text-xl font-semibold">Event Chart</h2>
      <canvas id="eventChart"></canvas>
    </section>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import Chart from 'chart.js/auto';

function useAeppService() {
  const fetchEventCount = async () => {
    const res = await fetch('/api/web/event-count');
    const data = await res.json();
    return data.count;
  };

  const fetchVisitors = async () => {
    const res = await fetch('/api/web/unique-visitors');
    const data = await res.json();
    return data.visitors;
  };

  const fetchSessions = async () => {
    const res = await fetch('/api/web/sessions');
    const data = await res.json();
    return data.sessions;
  };

  const fetchPopularPages = async () => {
    const res = await fetch('/api/web/popular-pages');
    return await res.json();
  };

  const triggerAgentCheck = async () => {
    const res = await fetch('/api/aepp/agents/monitor');
    return await res.json();
  };

  return {
    fetchEventCount,
    fetchVisitors,
    fetchSessions,
    fetchPopularPages,
    triggerAgentCheck,
  };
}

export default {
  setup() {
    const eventCount = ref(null);
    const uniqueVisitors = ref(null);
    const sessions = ref(null);
    const popularPages = ref([]);
    const agentLogs = ref([]);
    let chartInstance = null;

    const {
      fetchEventCount: fetchEventCountService,
      fetchVisitors: fetchVisitorsService,
      fetchSessions: fetchSessionsService,
      fetchPopularPages: fetchPopularPagesService,
      triggerAgentCheck: triggerAgentCheckService,
    } = useAeppService();

    const updateChart = () => {
      const ctx = document.getElementById('eventChart');
      if (!ctx) return;

      if (chartInstance) {
        chartInstance.destroy();
      }

      chartInstance = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: ['Events', 'Sessions'],
          datasets: [
            {
              label: 'Web Metrics',
              data: [eventCount.value || 0, sessions.value || 0],
              backgroundColor: ['#1e3a8a', '#059669'],
            },
          ],
        },
        options: {
          responsive: true,
          plugins: {
            legend: { display: true },
            title: { display: true, text: 'Event vs Session Metrics' },
          },
        },
      });
    };

    const fetchEventCount = async () => {
      eventCount.value = await fetchEventCountService();
      updateChart();
    };

    const fetchVisitors = async () => {
      uniqueVisitors.value = await fetchVisitorsService();
    };

    const fetchSessions = async () => {
      sessions.value = await fetchSessionsService();
      updateChart();
    };

    const fetchPopularPages = async () => {
      popularPages.value = await fetchPopularPagesService();
    };

    const triggerAgentCheck = async () => {
      agentLogs.value = await triggerAgentCheckService();
    };

    onMounted(() => {
      // Optionally, initialize chart or load initial data here if needed
    });

    return {
      eventCount,
      uniqueVisitors,
      sessions,
      popularPages,
      agentLogs,
      fetchEventCount,
      fetchVisitors,
      fetchSessions,
      fetchPopularPages,
      triggerAgentCheck,
    };
  },
};
</script>

<style>
.btn {
  @apply px-4 py-2 bg-black text-white rounded hover:bg-gray-800 transition;
}
</style>