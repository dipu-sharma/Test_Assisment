<template>
  <div class="space-y-6">
    <div class="flex justify-between items-center">
      <h2 class="text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Attendance Records</h2>
      <UButton to="/attendance/mark" color="primary" icon="i-lucide-plus">Mark Attendance</UButton>
    </div>

    <UCard>
      <div class="mb-4 flex flex-col sm:flex-row items-center justify-between gap-4">
        <!-- Date Filter (Server-side API) -->
        <UFormField label="Filter by Date" name="filter_date">
          <UInput
            v-model="filterDate"
            type="date"
            icon="i-lucide-calendar"
            clearable
            @clear="filterDate = ''"
          />
        </UFormField>

        <div class="text-sm text-gray-500 dark:text-gray-400">
          Showing {{ attendanceWithEmployee.length }} records
        </div>
      </div>

      <UTable :data="attendanceWithEmployee" :columns="columns" :loading="pendingAttendance || pendingEmployees">
        <template #status-cell="{ row }">
          <UBadge :color="row.original.status === 'Present' ? 'success' : 'error'" variant="subtle">
            <UIcon :name="row.original.status === 'Present' ? 'i-lucide-check-circle' : 'i-lucide-x-circle'" class="mr-1 w-3 h-3" />
            {{ row.original.status }}
          </UBadge>
        </template>
      </UTable>
    </UCard>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const config = useRuntimeConfig()
const columns = [
  { id: 'employee_name', accessorKey: 'employee_name', header: 'Employee Name' },
  { id: 'employee_id', accessorKey: 'employee_id', header: 'Employee ID' },
  { id: 'date', accessorKey: 'date', header: 'Date' },
  { id: 'status', accessorKey: 'status', header: 'Status' }
]

const filterDate = ref('')

// Use server-side filtering by passing date as a query parameter
const { data: attendanceData, pending: pendingAttendance, refresh } = await useFetch('/attendance/', {
  baseURL: config.public.apiBase,
  query: computed(() => ({
    date: filterDate.value || undefined
  })),
  key: 'attendance-list-api'
})

const { data: employeesData, pending: pendingEmployees } = await useFetch('/employees/', {
  baseURL: config.public.apiBase,
  key: 'employees-list-for-attendance'
})

const attendanceWithEmployee = computed(() => {
  if (!attendanceData.value || !employeesData.value) return []
  
  return attendanceData.value.map(record => {
    const employee = employeesData.value.find(e => e.id === record.employee_id)
    return {
      ...record,
      employee_name: employee ? employee.full_name : 'Unknown',
      employee_id: employee ? employee.employee_id : 'Unknown'
    }
  })
})
</script>
