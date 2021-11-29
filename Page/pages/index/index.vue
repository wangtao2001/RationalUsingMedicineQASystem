<template>
  <view>
	<view class="top">
	  <text class="cn-name">合理用药智能问答平台</text>
	  <text class="en-name">Intelligent Q &amp; A Platform for Rational Medicine Use</text>
	</view>
    <view class="container">
<!-- 		<view class="intro">
		  <text>更高效的服务，更智能的问答</text>
		</view> -->
		<view class="search">
			<input
			  placeholder="如果您有关于医药知识相关问题,请搜索"
			  v-model="question"	  
			/>
		  <button @click="submit">提交</button>
		</view>
	</view>
  </view>
</template>

<script>
export default {
  data() {
    return {
      question: "",
    };
  },
  methods: {
    submit() {
      // 空字符串提交
      if (this.question.trim().length == 0) {
        this.question = "";
      } else {
        // 跳转
        uni.navigateTo({
          url: `../details/details?question=${this.question}&type=0`
        });
      }
    },
  },
};
</script>

<style scoped>
.top {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	height: 110px;
	font-family: MicrosoftYaHei;
	color: #303030;
}

.cn-name {
	font-weight: 600;
	font-size: 40px;
}

.en-name {
	font-size: 20px;
}

.container {
	background: url(../../static/backGround/首页背景.jpg) 50% center / cover no-repeat;
	height: 500px;
	display: flex;
	justify-content: center;
	align-items: center;
}

.search {
  display: flex;
  justify-content: center;
}

.search input {
  height: 50px;
  width: 600px;
  background-color: #ffffff;
  border-radius: 4px 0 0 4px;
  padding-left: 40px;
  color: #757575;
  font-size: 18px;
}

.search input:hover{
	box-shadow: 0 0 14px 2px rgb(9 19 62 / 24%); 
}

.search button {
  height: 50px;
  width: 80px;
  background-color: #3A5FCD;
  margin: 0;
  border-radius: 0 4px 4px 0;
  color: #FFF;
  text-align: center;
  line-height: 50px;
  }

</style>