<template>
  <div class="space-y-6">
    <div class="flex items-center justify-between">
      <h2 class="text-3xl font-bold tracking-tight text-gray-900 dark:text-white">Dashboard</h2>
    </div>

    <!-- Dashboard Summary Widget (Counts) -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      <UCard class="bg-primary-50 dark:bg-primary-950/20">
        <div class="flex items-center gap-4">
          <div class="p-3 bg-primary-100 dark:bg-primary-900 rounded-lg">
            <UIcon name="i-lucide-users" class="w-6 h-6 text-primary-600 dark:text-primary-400" />
          </div>
          <div>
            <p class="text-sm font-medium text-gray-500 dark:text-gray-400">Total Employees</p>
            <h3 class="text-2xl font-bold text-gray-900 dark:text-white">{{ dashboardData?.summary?.total_employees || 0 }}</h3>
          </div>
        </div>
      </UCard>

      <UCard class="bg-green-50 dark:bg-green-950/20">
        <div class="flex items-center gap-4">
          <div class="p-3 bg-green-100 dark:bg-green-900 rounded-lg">
            <UIcon name="i-lucide-user-check" class="w-6 h-6 text-green-600 dark:text-green-400" />
          </div>
          <div>
            <p class="text-sm font-medium text-gray-500 dark:text-gray-400">Present Today</p>
            <h3 class="text-2xl font-bold text-gray-900 dark:text-white">{{ dashboardData?.summary?.present_today || 0 }}</h3>
          </div>
        </div>
      </UCard>

      <UCard class="bg-red-50 dark:bg-red-950/20">
        <div class="flex items-center gap-4">
          <div class="p-3 bg-red-100 dark:bg-red-900 rounded-lg">
            <UIcon name="i-lucide-user-x" class="w-6 h-6 text-red-600 dark:text-red-400" />
          </div>
          <div>
            <p class="text-sm font-medium text-gray-500 dark:text-gray-400">Absent Today</p>
            <h3 class="text-2xl font-bold text-gray-900 dark:text-white">{{ dashboardData?.summary?.absent_today || 0 }}</h3>
          </div>
        </div>
      </UCard>
    </div>

    <!-- Employee Statistics Table (Bonus Table Feature) -->
    <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
      <div class="lg:col-span-2">
        <UCard>
          <template #header>
            <div class="flex items-center gap-2 font-semibold">
              <UIcon name="i-lucide-bar-chart-3" class="w-5 h-5 text-primary-500" />
              Employee Performance (Total Present Days)
            </div>
          </template>
          <UTable :data="dashboardData?.employee_stats || []" :columns="columns" :loading="pending" />
        </UCard>
      </div>

      <!-- Quick Actions -->
      <div class="space-y-6">
        <UCard>
          <template #header>
            <div class="flex items-center gap-2 font-semibold">
              <UIcon name="i-lucide-zap" class="w-5 h-5 text-primary-500" />
              Quick Actions
            </div>
          </template>
          <div class="grid grid-cols-1 gap-3">
            <UButton to="/employees/add" color="primary" icon="i-lucide-user-plus" block>Add New Employee</UButton>
            <UButton to="/attendance/mark" color="neutral" variant="soft" icon="i-lucide-calendar-plus" block>Mark Today's Attendance</UButton>
            <div class="border-t border-gray-200 dark:border-gray-800 my-1" />
            <UButton to="/employees" color="neutral" variant="ghost" icon="i-lucide-users" block>View All Employees</UButton>
            <UButton to="/attendance" color="neutral" variant="ghost" icon="i-lucide-clipboard-list" block>View All Records</UButton>
          </div>
        </UCard>
      </div>
    </div>
  </div>
</template>

<script setup>
const config = useRuntimeConfig()

const columns = [
  { id: 'employee_name', accessorKey: 'employee_name', header: 'Employee Name' },
  { id: 'total_present_days', accessorKey: 'total_present_days', header: 'Total Present Days' }
]

// Fetch dashboard summary from the server-side API
const { data: dashboardData, pending } = await useFetch('/dashboard/summary', {
  baseURL: config.public.apiBase,
  key: 'dashboard-summary-page'
})
</script>
