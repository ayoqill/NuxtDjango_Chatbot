<template>
  <div class="flex flex-col h-full">
    <ScrollArea class="flex-1 px-4 py-4">
      <!-- Empty State -->
      <div
        v-if="messages.length === 0"
        class="h-full flex flex-col items-center justify-center text-muted-foreground gap-2"
      >
        <MessageCircleOff class="size-10" />
        <p class="text-sm">Start a conversation...</p>
      </div>

      <!-- Messages -->
      <div v-else class="space-y-4">
        <div
          v-for="(msg, idx) in messages"
          :key="idx"
          :class="['flex', msg.role === 'user' ? 'justify-end' : 'justify-start']"
        >
          <div
            :class="[
              'max-w-[75%] rounded-2xl px-3 py-2 text-sm leading-relaxed',
              msg.role === 'user'
                ? 'bg-primary text-primary-foreground rounded-br-sm'
                : 'bg-muted text-foreground rounded-bl-sm'
            ]"
          >
            {{ msg.text }}
          </div>
        </div>

        <!-- Typing Indicator -->
        <div v-if="isLoading" class="flex justify-start">
          <div class="bg-muted rounded-2xl rounded-bl-sm px-4 py-2 flex items-center gap-1">
            <span class="size-1.5 bg-muted-foreground rounded-full animate-bounce" style="animation-delay: 0ms" />
            <span class="size-1.5 bg-muted-foreground rounded-full animate-bounce" style="animation-delay: 150ms" />
            <span class="size-1.5 bg-muted-foreground rounded-full animate-bounce" style="animation-delay: 300ms" />
          </div>
        </div>

        <div ref="sentinel" />
      </div>
    </ScrollArea>

    <!-- Input Row -->
    <div class="border-t p-4">
      <div class="flex gap-2">
        <input
          v-model="input"
          placeholder="Type a message..."
          :disabled="isLoading"
          class="flex-1 h-8 rounded-lg border border-input bg-transparent px-2.5 py-1 text-sm"
          @keyup.enter="sendMessage"
        />
        <button
          @click="sendMessage"
          :disabled="!input.trim() || isLoading"
          class="inline-flex items-center justify-center h-8 px-2.5 rounded-lg bg-primary text-primary-foreground text-sm font-medium disabled:opacity-50 disabled:pointer-events-none"
        >
          <Send class="size-4" />
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { Send, MessageCircleOff } from '@lucide/vue'

const messages = ref<{ role: 'user' | 'bot'; text: string }[]>([])
const input = ref('')
const isLoading = ref(false)
const sentinel = ref<HTMLElement | null>(null)

function scrollToBottom() {
  nextTick(() => {
    sentinel.value?.scrollIntoView({ behavior: 'smooth' })
  })
}

watch(messages, scrollToBottom, { deep: true })
watch(isLoading, scrollToBottom)

function sendMessage() {
  const text = input.value.trim()
  if (!text || isLoading.value) return

  messages.value.push({ role: 'user', text })
  input.value = ''
  isLoading.value = true

  setTimeout(() => {
    messages.value.push({ role: 'bot', text: `You said: ${text}` })
    isLoading.value = false
  }, 1500)
}
</script>
