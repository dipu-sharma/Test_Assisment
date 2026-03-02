<template>
  <div class="max-w-2xl mx-auto py-8 px-4">
    <div class="mb-8 flex items-center justify-between">
      <div class="flex items-center gap-4">
        <UButton
          to="/employees"
          variant="ghost"
          color="neutral"
          icon="i-lucide-arrow-left"
          class="rounded-full"
        />
        <div>
          <h2 class="text-3xl font-extrabold text-gray-900 dark:text-white tracking-tight">
            Add New Employee
          </h2>
          <p class="text-sm text-gray-500 dark:text-gray-400">
            Create a new record in the personnel management system.
          </p>
        </div>
      </div>
    </div>

    <UCard class="shadow-xl ring-1 ring-gray-200 dark:ring-gray-800">
      <template #header>
        <div class="flex items-center gap-2 text-primary-600 dark:text-primary-400 font-semibold">
          <UIcon name="i-lucide-user-plus" class="w-5 h-5" />
          Employee Information
        </div>
      </template>

      <UForm :state="state" @submit="onSubmit" class="space-y-6">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <UFormField label="Employee ID" name="employee_id" required help="Unique identification number">
            <UInput
              v-model="state.employee_id"
              placeholder="e.g. EMP-001"
              icon="i-lucide-id-card"
              size="lg"
              class="w-full"
            />
          </UFormField>

          <UFormField label="Full Name" name="full_name" required>
            <UInput
              v-model="state.full_name"
              placeholder="John Doe"
              icon="i-lucide-user"
              size="lg"
              class="w-full"
            />
          </UFormField>
        </div>

        <UFormField label="Email Address" name="email_address" required>
          <UInput
            v-model="state.email_address"
            type="email"
            placeholder="john.doe@company.com"
            icon="i-lucide-mail"
            size="lg"
            class="w-full"
          />
        </UFormField>

        <UFormField label="Department" name="department" required>
          <UInput
            v-model="state.department"
            placeholder="Engineering, HR, Sales..."
            icon="i-lucide-briefcase"
            size="lg"
            class="w-full"
          />
        </UFormField>

        <div class="border-t border-gray-200 dark:border-gray-800 my-6" />

        <div class="flex justify-end items-center gap-3 pt-2">
          <UButton
            to="/employees"
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
            icon="i-lucide-check"
          >
            Create Employee
          </UButton>
        </div>
      </UForm>
    </UCard>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useApi } from '~/composables/useApi'

const { $api } = useApi()
const router = useRouter()

const state = ref({
  employee_id: '',
  full_name: '',
  email_address: '',
  department: ''
})

const loading = ref(false)

const onSubmit = async () => {
  loading.value = true
  try {
    await $api('/employees/', {
      method: 'POST',
      body: state.value
    })
    router.push('/employees')
  } catch (error) {
    alert(error.data?.detail || 'Failed to add employee')
  } finally {
    loading.value = false
  }
}
</script>
