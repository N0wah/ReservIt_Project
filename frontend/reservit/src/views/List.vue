<template>
    <div class="min-h-screen bg-[#242424] flex flex-col justify-start px-6 py-8 font-poppins">
      
      <!-- Logo / titre -->
      <div class="flex justify-center">
        <h2 class="font-carattere italic text-[50px] mb-2 text-center text-white">
          <span class="text-orange-400">R</span>eservation
        </h2>
      </div>

      <ul class="list-none flex flex-col gap-2 z-0">
        <li>
            <Bookitems :lat="48.8584" :lng="2.2945"  />
        </li>
        <li>
            <Bookitems :lat="48.8584" :lng="2.2945"  />
        </li>
        <li>
            <Bookitems :lat="48.8584" :lng="2.2945"  />
        </li>
        <li>
            <Bookitems :lat="48.8584" :lng="2.2945"  />
        </li>
        <li>
            <Bookitems :lat="48.8584" :lng="2.2945"  />
        </li>


      </ul>


    </div>


</template>

<script setup>
 import Bookitems from '../components/Bookitems.vue'
</script>