<template>
     <div class="bg-[#242424] min-h-screen text-white px-4 pt-6 pb-24">
      
      <!-- Logo / titre -->
       <div class="flex justify-center items-center gap-2">
      <div class="flex justify-center">
        <h2 class="font-carattere italic text-[50px] mb-2 text-center text-white">
          <span class="text-orange-400">R</span>eservation
        </h2>
        
        </div>
        <p><span class="text-orange-400">A</span>dmin</p>
        </div>
        <ul class="list-none flex flex-col gap-2 z-0">
        <li>
            <Bookitems :lat="48.8584" :lng="2.2945"  />
        </li>
        </ul>



    </div>
    <RestaurantNav />
</template>
<script setup>
import Bookitems from '@/components/RestaurantBookitems.vue';
import NavComposant from '@/components/NavComposant.vue';
import RestaurantNav from '@/components/RestaurantNav.vue';


</script>