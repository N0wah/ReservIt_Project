<template>
    <RestaurantNav />
    <div class="bg-[#242424] min-h-screen text-white px-6 pt-6 pb-24">
        <div class="flex justify-center items-center gap-2">
      <div class="flex justify-center">
        <h2 class="font-carattere italic text-[50px] mb-2 text-center text-white">
          <span class="text-orange-400">D</span>ashboard
        </h2>
        
        </div>
        <p><span class="text-orange-400">A</span>dmin</p>
        </div>
        <section class="mb-3">
    <h1 class="font-Poppins text-lg">Weekly Reservation</h1>
    <RestaurantGraphic />
        </section>
        <section>
    <h1 class="font-Poppins text-lg">Lastest Customers Reservation</h1>
    <ul>
        <li class=" list-none flex flex-col gap-2 z-0">
            <RestaurantBookitems />
            <RestaurantBookitems />
            <RestaurantBookitems />
            <RestaurantBookitems />
        </li>
    </ul>
    </section>
    </div>
</template>

<script setup>
import RestaurantNav from '@/components/RestaurantNav.vue';
import RestaurantGraphic from '@/components/RestaurantGraphic.vue';
import RestaurantBookitems from '@/components/RestaurantBookitems.vue';
</script>