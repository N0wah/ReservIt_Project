import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'
import tailwindcss from '@tailwindcss/vite'

// https://vite.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    tailwindcss(),
    {
      name: 'vite-plugin-remove-debugger',
      enforce: 'pre',
      transform(code, id) {
        if (id.endsWith('.html')) {
          return code.replace(/<div[^>]*class="vite-plugin[^"]*"[^>]*><\/div>/g, '')
        }
        return code
      }
    }
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    },
  },
})
