<template>
  <div class="min-h-screen bg-background flex items-center justify-center p-4">
    <Card class="w-full max-w-lg h-[90vh] flex flex-col">
      <CardHeader class="border-b px-4 py-3 flex items-center justify-center gap-2">
        <CardTitle class="text-xl font-semibold tracking-tight">Fake Chatbot</CardTitle>
      </CardHeader>
      <CardContent class="flex-1 p-0 overflow-hidden">
        <ChatBox />
      </CardContent>
    </Card>
  </div>
</template>
