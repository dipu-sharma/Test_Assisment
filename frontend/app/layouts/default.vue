<template>
  <div class="min-h-screen bg-gray-50 dark:bg-gray-900">
    <header class="bg-white dark:bg-gray-800 border-b border-gray-200 dark:border-gray-700 p-4 sticky top-0 z-50">
      <div class="max-w-7xl mx-auto flex items-center justify-between">
        <h1 class="text-xl font-bold text-gray-900 dark:text-white flex items-center gap-2">
          HRMS Lite
        </h1>
        <nav class="flex gap-4">
          <UButton to="/" variant="ghost" color="neutral">Dashboard</UButton>
          <UButton to="/employees" variant="ghost" color="neutral">Employees</UButton>
          <UButton to="/attendance" variant="ghost" color="neutral">Attendance</UButton>
        </nav>
      </div>
    </header>

    <main class="max-w-7xl mx-auto p-4 sm:p-6 lg:p-8">
      <slot />
    </main>
  </div>
</template>
