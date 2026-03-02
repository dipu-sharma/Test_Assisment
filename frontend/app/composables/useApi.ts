export const useApi = () => {
  const config = useRuntimeConfig()
  
  const $api = $fetch.create({
    baseURL: config.public.apiBase,
    onRequest({ request, options }) {
      // Add custom headers if needed
    },
    onResponseError({ response }) {
      // Global error handling
      console.error('API Error:', response._data?.detail || response.statusText)
    }
  })

  return { $api }
}
