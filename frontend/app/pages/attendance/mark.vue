<template>
  <div class="max-w-2xl mx-auto py-8 px-4">
    <div class="mb-8 flex items-center justify-between">
      <div class="flex items-center gap-4">
        <UButton
          to="/attendance"
          variant="ghost"
          color="neutral"
          icon="i-lucide-arrow-left"
          class="rounded-full"
        />
        <div>
          <h2 class="text-3xl font-extrabold text-gray-900 dark:text-white tracking-tight">
            Mark Attendance
          </h2>
          <p class="text-sm text-gray-500 dark:text-gray-400">
            Record the daily status for an employee.
          </p>
        </div>
      </div>
    </div>

    <UCard class="shadow-xl ring-1 ring-gray-200 dark:ring-gray-800">
      <template #header>
        <div class="flex items-center gap-2 text-primary-600 dark:text-primary-400 font-semibold">
          <UIcon name="i-lucide-calendar-check" class="w-5 h-5" />
          Attendance Details
        </div>
      </template>

      <UForm :state="state" @submit="onSubmit" class="space-y-6">
        <UFormField label="Select Employee" name="employee_id" required help="Choose an employee from the list">
          <USelectMenu
            v-model="state.employee_id"
            :items="employeeOptions"
            value-key="value"
            placeholder="Search for an employee..."
            icon="i-lucide-users"
            size="lg"
            class="w-full"
            :loading="pendingEmployees"
          />
        </UFormField>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <UFormField label="Date" name="date" required>
            <UInput
              v-model="state.date"
              type="date"
              icon="i-lucide-calendar"
              size="lg"
              class="w-full"
            />
          </UFormField>

          <UFormField label="Status" name="status" required>
            <USelect
              v-model="state.status"
              :items="statusOptions"
              icon="i-lucide-check-circle"
              size="lg"
              class="w-full"
            />
          </UFormField>
        </div>

        <div class="border-t border-gray-200 dark:border-gray-800 my-6" />

        <div class="flex justify-end items-center gap-3 pt-2">
          <UButton
            to="/attendance"
            variant="subtle"
            color="neutral"
            size="lg"
          >
            Cancel
          </UButton>
          <UButton
            type="submit"
            color="primary"
            size="lg"
            :loading="loading"
            icon="i-lucide-save"
          >
            Save Record
          </UButton>
        </div>
      </UForm>
    </UCard>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useApi } from '~/composables/useApi'

const { $api } = useApi()
const config = useRuntimeConfig()
const router = useRouter()

const { data: employees, pending: pendingEmployees, error } = await useFetch('/employees/', {
  baseURL: config.public.apiBase,
  key: 'employees-fetch-key'
})

const employeeOptions = computed(() => {
  const list = employees.value || []
  return list.map(emp => ({
    label: emp.full_name || 'Unknown Name',
    value: emp.id
  }))
})

const statusOptions = [
  { label: 'Present', value: 'Present' },
  { label: 'Absent', value: 'Absent' }
]

const today = new Date().toISOString().split('T')[0]

const state = ref({
  employee_id: null,
  date: today,
  status: 'Present'
})

const loading = ref(false)

const onSubmit = async () => {
  if (!state.value.employee_id) {
    alert('Please select an employee')
    return
  }
  
  loading.value = true
  try {
    await $api('/attendance/', {
      method: 'POST',
      body: state.value
    })
    router.push('/attendance')
  } catch (error) {
    alert(error.data?.detail || 'Failed to mark attendance')
  } finally {
    loading.value = false
  }
}
</script>
