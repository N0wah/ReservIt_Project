<template>
  <v-calendar
  class="mt-[-1vh] shadow-[1px_3px_3.7px_rgba(0,0,0,0.25)]"
    title-position="left"
    expanded
    :attributes="attributes"
    @dayclick="onDayClick"
    :style="$style.calendar"
  />
</template>

<script>
import { ref, watch } from 'vue';

export default {
  setup() {
    const selectedDate = ref(null);
    const attributes = ref([
      {
        key: 'selected',
        highlight: {
          color: 'orange',
          fillMode: 'solid',
        },
        dates: selectedDate.value,
      },
    ]);

    watch(selectedDate, (newVal) => {
      attributes.value[0].dates = newVal;
    });

    const onDayClick = (day) => {
      selectedDate.value = day.date;
    };

    return { selectedDate, attributes, onDayClick };
  },
};
</script>

<style module>
.calendar {
  --vc-bg: #444444;
  --vc-text: #EBEBEB;
  --vc-border: #555555;
  --vc-accent-50: #555555;
  --vc-accent-100: #666666;
  --vc-accent-200: #777777;
  --vc-accent-300: #888888;
  --vc-accent-400: #999999;
  --vc-accent-500: #AAAAAA;
  --vc-accent-600: #EBEBEB;
  --vc-accent-700: #CCCCCC;
  --vc-accent-800: #DDDDDD;
  --vc-accent-900: #EEEEEE;

  background-color: var(--vc-bg) !important;
  color: var(--vc-text) !important;
  border-radius: 8px;
  padding: 10px;
}

.calendar :global(.vc-title) {
  color: var(--vc-accent-600) !important;
  font-weight: bold;
}

.calendar :global(.vc-header) {
  color: var(--vc-accent-600) !important;
  border-bottom: 1px solid var(--vc-border);
}

.calendar :global(.vc-day-content:not(.is-not-in-month)) {
  color: var(--vc-text) !important;
}

.calendar :global(.vc-highlight) {
  background-color: orange !important;
  color: black !important;
}

.calendar :global(.vc-day-content:hover) {
  background-color: var(--vc-accent-100) !important;
}

.calendar :global(.vc-arrow:hover) {
  background-color: var(--vc-accent-100) !important;
}

.calendar :global(.vc-day-content.is-not-in-month) {
  color: var(--vc-accent-400) !important;
  opacity: 0.6;
}

/* À ajouter dans votre style global */

</style>