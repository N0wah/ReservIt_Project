<template>
  <div class="bg-[#242424] min-h-screen text-white px-4 pt-6 ">
    <div class="relative w-full h-[85vh] sm:h-[600px] ">
      <!-- Image plein écran -->
      <img
        src="../assets/food.png"
        alt="Delicious food"
        class="absolute top-0 left-0 w-full h-full object-cover rounded-4xl"
      />

      <!-- Overlay sombre pour lisibilité -->
      <div class="absolute top-0 left-0 w-full h-full  bg-opacity-25 z-10"></div>

      <!-- Texte et bouton superposés -->
      <div class="absolute bottom-0 w-full px-6 pb-10 text-white z-20">
        <h2 class="font-carattere italic text-[40px] mb-2 sm:text-left">
          <span class="text-orange-400">R</span>eserv'<span class="text-orange-400">I</span>t
        </h2>
        <p class="text-sm mb-6">
          Let’s you easily book your favorite restaurants and discover new spots we’ve handpicked just for you!
        </p>
      </div>
    </div>

    <!-- Bouton en dehors de l'image -->
    <button
      class="mt-6 bg-orange-500 text-white text-lg  py-3 w-full rounded-full font-Poppins font-light"
      @click="$router.push('/home')"
    >
      Let’s Reserve It
    </button>
  </div>
</template>
