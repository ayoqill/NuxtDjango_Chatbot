# This is for Authorization: Bearer access_token header in the request to access protected endpoints.

<template>
  <div class="min-h-screen flex items-center justify-center bg-muted">
    <div class="w-full max-w-sm rounded-xl border bg-background p-6 shadow">
      <h1 class="text-2xl font-bold mb-4 text-center">Login</h1>

      <form @submit.prevent="login" class="space-y-4">
        <div>
          <label class="text-sm font-medium">Username</label>
          <input
            v-model="username"
            type="text"
            class="w-full border rounded-lg px-3 py-2 mt-1"
            placeholder="Enter username"
          />
        </div>

        <div>
          <label class="text-sm font-medium">Password</label>
          <input
            v-model="password"
            type="password"
            class="w-full border rounded-lg px-3 py-2 mt-1"
            placeholder="Enter password"
          />
        </div>

        <button
          type="submit"
          :disabled="isLoading"
          class="w-full bg-primary text-primary-foreground rounded-lg py-2 disabled:opacity-50"
        >
          {{ isLoading ? "Logging in..." : "Login" }}
        </button>

        <p v-if="errorMessage" class="text-red-500 text-sm text-center">
          {{ errorMessage }}
        </p>
      </form>
    </div>
  </div>
</template>

<script setup lang="ts">
const username = ref("")
const password = ref("")
const isLoading = ref(false)
const errorMessage = ref("")

async function login() {
  if (!username.value || !password.value) {
    errorMessage.value = "Please enter username and password"
    return
  }

  isLoading.value = true
  errorMessage.value = ""

  try {
    const response = await $fetch<{
      access: string
      refresh: string
    }>("http://127.0.0.1:8000/api/token/", {
      method: "POST",
      body: {
        username: username.value,
        password: password.value,
      },
    })

    localStorage.setItem("access_token", response.access)
    localStorage.setItem("refresh_token", response.refresh)

    await navigateTo("/")
  } catch (error) {
    errorMessage.value = "Invalid username or password"
  } finally {
    isLoading.value = false
  }
}
</script>