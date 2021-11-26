<template>
  <view class="w">
    <view class="top">
      <view class="title" @click="navigateToIndex">
        <text class="title1">合理用药智能问答平台</text>
        <text class="title2"
          >Intelligent Q & A platform for rational drug use</text
        >
      </view>
      <view class="search">
        <input placeholder="如果您有关于医药知识相关问题,请搜索" />
        <button>提交</button>
      </view>
    </view>
    <view class="answer">
      <text class="answer-tip">问题的答案为:</text>
      <text class="answer-item">{{ answer }}</text>
    </view>
    <view class="viz-container">
      <view class="viz"></view>
    </view>
  </view>
</template>

<script>
import NeoVis from "../../static/js/neovis.js";
import NeoVisConfig from "../../static/js/neovis-config.js"

export default {
  data() {
    return {
      answer: "",
    };
  },
  onLoad: function (option) {
    if (option.type == "0") {
      // 问题提交
      console.log(option.question);
      this.getAnswer(option.question);
    } else if (option.type == "1") {
      // 快捷导航提交
      console.log(option.title);
    }
    // 渲染可视化图谱
    var viz =  new NeoVis(NeoVisConfig); // 不使用NeoVis.default构造器
    viz.render();
    console.log("render finished");
  },
  methods: {
    navigateToIndex() {
      uni.navigateTo({
        url: "../index/index",
        success: () => {
          console.log("跳转成功");
        },
        fail: () => {
          console.log("跳转失败");
        },
      });
    },
    // 向后端发请求
    getAnswer(question) {
      uni.request({
        url: "http://127.0.0.1:8000/answer",
        method: "POST",
        header: {
          "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
        },
        data: {
          question: question,
        },
        dataType: "json",
        success: (res) => {
          this.answer = res.data.answer;
        },
      });
    },
  },
};
</script>

<style>
	.w {
	width: 80%;
	margin: 10px auto;
}

	.top {
	display: flex;
	justify-content: space-between;
	margin-bottom: 20px;
	}

	.title {
	width: 40%;
	display: flex;
	flex-wrap: wrap;
	align-content: flex-start;
	font-weight: 600;
	}

	.title1 {
	color: #00008b;
	font-size: 20px;
	font-family: Simsun;
	text-align: center;
	}

	.title2 {
	color: #4f4f4f;
	font-size: 15px;
	font-family: Simsun;
	}

	.search {
	display: flex;
	justify-content: flex-end;
	font-size: 5px;
	}

	.search input {
	border: #007aff solid 1px;
	height: 30px;
	width: 300px;
	}

	.search button {
	height: 30px;
	}

	.answer {
	font-size: 15px;
	color: #333333;
	display: flex;
	flex-direction: column;
	}

	.answer-tip {
	margin-bottom: 10px;
	}
	.viz {
	height: 200px;
	width: 200px;
	border: #00008b 1px solid;
	}
</style>
