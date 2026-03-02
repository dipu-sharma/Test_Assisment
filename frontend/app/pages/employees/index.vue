<template>
  <div class="space-y-6">
    <div class="flex justify-between items-center">
      <h2 class="text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Employees Directory</h2>
      <UButton to="/employees/add" color="primary" icon="i-lucide-user-plus">Add Employee</UButton>
    </div>

    <UCard>
      <UTable :data="employeesWithAttendance || []" :columns="columns" :loading="pendingEmployees || pendingDashboard">
        <template #total_present-cell="{ row }">
          <UBadge color="primary" variant="soft">
            {{ row.original.total_present }} Days
          </UBadge>
        </template>
        
        <template #actions-cell="{ row }">
          <UButton 
            color="red" 
            variant="ghost" 
            icon="i-lucide-trash-2" 
            size="sm"
            @click="deleteEmployee(row.original.id)" 
          />
        </template>
      </UTable>
    </UCard>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useApi } from '~/composables/useApi'

const { $api } = useApi()
const config = useRuntimeConfig()

const columns = [
  { id: 'employee_id', accessorKey: 'employee_id', header: 'Employee ID' },
  { id: 'full_name', accessorKey: 'full_name', header: 'Full Name' },
  { id: 'department', accessorKey: 'department', header: 'Department' },
  { id: 'email_address', accessorKey: 'email_address', header: 'Email' },
  { id: 'total_present', accessorKey: 'total_present', header: 'Total Present Days' },
  { id: 'actions', accessorKey: 'id', header: 'Actions' }
]

const { data: employees, pending: pendingEmployees, refresh } = await useFetch('/employees/', {
  baseURL: config.public.apiBase,
  key: 'employees-directory-api'
})

// Fetch server-side aggregated stats from the dashboard summary
const { data: dashboardData, pending: pendingDashboard } = await useFetch('/dashboard/summary', {
  baseURL: config.public.apiBase,
  key: 'dashboard-summary-for-directory'
})

const employeesWithAttendance = computed(() => {
  if (!employees.value) return []
  
  return employees.value.map(emp => {
    // Map stats from dashboardData
    const stats = dashboardData.value?.employee_stats?.find(s => s.employee_id === emp.id)
    return {
      ...emp,
      total_present: stats ? stats.total_present_days : 0
    }
  })
})

const deleteEmployee = async (id) => {
  if (confirm('Are you sure you want to delete this employee? This will also remove their attendance records.')) {
    try {
      await $api(`/employees/${id}`, {
        method: 'DELETE'
      })
      await refresh()
    } catch (e) {
      alert('Error deleting employee')
    }
  }
}
</script>
