<template>
  <div class="avatar-wrapper" :style="wrapperStyle">
    <img v-if="src" :src="avatarSrc" :alt="alt" class="avatar-img" />
  </div>
</template>

<script setup>
import { computed } from 'vue'

const props = defineProps({
  src: { type: String, default: '' },
  alt: { type: String, default: 'User avatar' },
  size: { type: [String, Number], default: 128 },
  rounded: { type: Boolean, default: true },
})

console.log('Avatar src:', props.src)
const avatarSrc = computed(() => {
  if (!props.src) return '/img/avatar/default.png'  // <-- image par défaut
  return props.src.startsWith('/') ? props.src : '/' + props.src
})

const wrapperStyle = computed(() => ({
  width: typeof props.size === 'number' ? props.size + 'px' : props.size,
  height: typeof props.size === 'number' ? props.size + 'px' : props.size,
  borderRadius: props.rounded ? '9999px' : '8px',
  background: '#fff',
  overflow: 'hidden',
  display: 'flex',
  alignItems: 'center',
  justifyContent: 'center',
}))
</script>


<style scoped>
.avatar-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}
.avatar-placeholder {
  color: #bbb;
  font-size: 2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%;
  background: #eee;
}
</style>
