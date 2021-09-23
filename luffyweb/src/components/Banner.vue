<template>
  <div class="banner">
    <el-carousel height="400px">
      <el-carousel-item v-for="item in banner_list" :key="item">
        <div v-if="item.link.startsWith('http')">
          <a :href="item.link"><img :src="item.image" :alt="item.title"></a>
        </div>
        <div v-else>
          <router-link :to="item.link"><img :src="item.image" :alt="item.title"></router-link>
        </div>
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>

export default {
  name: "Header",
  data() {
    return {
      banner_list: []
    }
  },
  created() {
    this.$axios.get(this.$url.base_url + 'home/banner/').then(res => {
      this.banner_list = res.data
      console.log(this.banner_list)
    })
  }
}
</script>

<style scoped>
.el-carousel__item {
  height: 400px;
  min-width: 1200px;
}

.el-carousel__item img {
  height: 400px;
  margin-left: calc(50% - 1920px / 2);
}
</style>