<template>
  <div class="chatbox">
    <div class="messages" ref="messagesContainer">
      <div
        v-for="(msg, idx) in messages"
        :key="idx"
        :class="['bubble', msg.role]"
      >
        {{ msg.text }}
      </div>
      <div v-if="isLoading" class="bubble bot typing">
        Bot is typing...
      </div>
    </div>
    <div class="input-row">
      <input
        v-model="input"
        type="text"
        placeholder="Type a message..."
        @keyup.enter="sendMessage"
        :disabled="isLoading"
      />
      <button @click="sendMessage" :disabled="isLoading || !input.trim()">
        Send
      </button>
    </div>
  </div>
</template>

<script setup>
const messages = ref([])
const input = ref('')
const isLoading = ref(false)
const messagesContainer = ref(null)

function sendMessage() {
  const text = input.value.trim()
  if (!text || isLoading.value) return

  messages.value.push({ role: 'user', text })
  input.value = ''
  isLoading.value = true

  scrollToBottom()

  setTimeout(() => {
    messages.value.push({ role: 'bot', text: `You said: ${text}` })
    isLoading.value = false
    nextTick(() => scrollToBottom())
  }, 1500)
}

function scrollToBottom() {
  nextTick(() => {
    if (messagesContainer.value) {
      messagesContainer.value.scrollTop = messagesContainer.value.scrollHeight
    }
  })
}
</script>

<style scoped>
.chatbox {
  flex: 1;
  display: flex;
  flex-direction: column;
  border: 1px solid #ccc;
  border-radius: 8px;
  overflow: hidden;
}

.messages {
  flex: 1;
  overflow-y: auto;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.bubble {
  max-width: 75%;
  padding: 0.5rem 1rem;
  border-radius: 16px;
  word-wrap: break-word;
}

.bubble.user {
  align-self: flex-end;
  background: #007aff;
  color: #fff;
  border-bottom-right-radius: 4px;
}

.bubble.bot {
  align-self: flex-start;
  background: #e9e9eb;
  color: #000;
  border-bottom-left-radius: 4px;
}

.bubble.typing {
  font-style: italic;
  opacity: 0.7;
}

.input-row {
  display: flex;
  border-top: 1px solid #ccc;
  padding: 0.5rem;
  gap: 0.5rem;
}

.input-row input {
  flex: 1;
  padding: 0.5rem 0.75rem;
  border: 1px solid #ccc;
  border-radius: 20px;
  outline: none;
  font-size: 1rem;
}

.input-row input:disabled {
  background: #f5f5f5;
}

.input-row button {
  padding: 0.5rem 1.25rem;
  border: none;
  border-radius: 20px;
  background: #007aff;
  color: #fff;
  font-size: 1rem;
  cursor: pointer;
}

.input-row button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}
</style>
