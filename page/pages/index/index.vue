<template>
  <view>
    <view class="top-title">
      <text class="title1">合理用药智能问答平台</text>
    </view>
    <view class="englishName">
      <text class="title2">Intelligent Q &amp; A platform for rational drug use</text>
    </view>
    <image
      class="beijing"
      src="../../static/backGround/首页背景.jpg"
      mode="aspectFill"
    ></image>
    <!-- 介绍 -->
    <view class="text-area">
      <text class="title">-更高效的服务，更智能的问答-</text>
    </view>
    <view class="uni-form-item uni-column">
		<input
		  class="uni-input"
		  placeholder="如果您有关于医药知识相关问题,请搜索"
		  v-model="question"	  
		/>
      <button @click="submit">提交</button>
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
          url: `../details/details?question=${this.question}&type=0`,
          success: () => {
            console.log("跳转成功");
          },
          fail: () => {
            console.log("跳转失败");
          },
        });
      }
    },
  },
};
</script>

<style>
.top-title {
  color: #00008b;
  font-size: 40px;
  font-family: Simsun;
  display: flex;
  justify-content: center;
}
.englishName {
  color: #4f4f4f;
  font-size: 20px;
  font-family: Simsun;
  display: flex;
  justify-content: center;
}
.uni-form-item {
  display: flex;
  justify-content: center;
  margin-top: 80px;
}
input {
  height: 40px;
  width: 300px;
  background-color: #ffffff;
}
button {
  height: 40px;
  width: 80px;
  background-color: #4876ff;
  margin: 0;
}
.beijing {
  height: 100%;
  width: 100%;
  position: fixed;
  top: 15;
  z-index: -1;
}
.text-area {
  color: #ffffff;
  font-size: 40rpx;
  margin-top: 80px;
  margin-left: 30px;
}
</style>