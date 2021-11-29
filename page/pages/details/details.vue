<template>
  <view class="w">
    <view class="top">
      <view class="title" @click="navigateToTab('index')">
        <text class="cn-name">合理用药智能问答平台</text>
        <text class="en-name"
          >Intelligent Q &amp; A Platform for Rational Medicine Use</text
        >
      </view>
      <view class="search">
        <input placeholder="如果您有关于医药知识相关问题,请搜索" v-model="topQuestion"/>
        <button onclick="topSubmit">提交</button>
      </view>
    </view>
	<view class="navi">
		<view class="a" @click="navigateToTab('index')">首页</view>
		<view class="b" onclick="javascript:location.reload();">查询详情</view>
		<view @click="navigateToTab('depart')">科室</view>
		<view @click="navigateToTab('dialectics')">辩证法</view>
		<view @click="navigateToTab('medicine')">中药</view>
	</view>
   <view class="answer">
		<view class="answer-card">
			<view class="answer-tip">
				<image src="../../static/answerCard/编辑.png"></image>
				<text>问题的答案为:</text>
			</view>
			<view class="answer-content">
				<text>{{answer}}</text>
			</view>
			<view class="answer-action">
				<view class="answer-action-item">
					<image src="../../static/answerCard/分享.png"></image>
					<text>分享</text>
				</view>
				<view class="answer-action-item" @click="actionLike">
					<image :src="likeIcon"></image>
					<text>点赞</text>
				</view>
				<view class="answer-action-item">
					<image src="../../static/answerCard/评论.png"></image>
					<text>评论</text>
				</view>
			</view>
		</view>
	    <view class="viz-container">
	       <view id="viz"></view>
	     </view>
	   </view>
   </view>
</template>

<script>
import NeoVis from "../../static/js/neovis.js";
import NeoVisConfig from "../../static/js/neovis-config.js"; // 图谱配置文件

export default {
  data() {
    return {
      answer: "",
	  topQuestion: "",
	  likeIcon: "../../static/answerCard/点赞.png",
	  like: false
    };
  },
  // 页面启动时
  onLoad: function (option) {
    if (option.type == "0") {
      // 问题提交
      console.log(option.question);
      this.getAnswer(option.question, option.type);
    } else {
      // 快捷导航提交
	  this.getAnswer(option.title, option.type);
    }
  },
  methods: {
	// 跳转TabBar
	navigateToTab(path) {
		uni.switchTab({
			url: `../${path}/${path}`
		})
	},
    // 向后端发请求
    getAnswer(questionOrTitle, type) {
      uni.request({
        url: "http://127.0.0.1:8000/answer",
        method: "POST",
        header: {
          "Content-Type": "application/x-www-form-urlencoded;charset=utf-8",
        },
        data: {
          questionOrTitle: questionOrTitle,
		  type: type
        },
        dataType: "json",
        success: (res) => {
		  // 后端获取问题答案和图谱查询语句
		  // 将数据展示出来
          this.answer = res.data.answer;
		  NeoVisConfig['initial_cypher'] = res.data.cypher;
		  this.drawNeo();
        },
      });
    },
	// 渲染可视化图谱
	drawNeo() {
		var viz = new NeoVis(NeoVisConfig); // 不使用NeoVis.default构造器
		viz.render();
		console.log("render finished");
	},
	// 顶部搜索框
	topSubmit() {
		if (this.topQuestion.trim().length == 0) {
		  this.topQuestion = "";
		} else {
			this.getAnswer(this.topQuestion)
		}
	},
	// 点赞动作
	actionLike() {
		if ( !this.like) {
			this.likeIcon = "../../static/answerCard/点赞-active.png"
		} else {
			this.likeIcon = "../../static/answerCard/点赞.png"
		}
		this.like = !this.like
	}
  },
};
</script>

<style scoped>
.w {
  width: 80%;
  margin: 10px auto;
}

.top {
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 90px;
}

.title {
  width: 40%;
  display: flex;
  flex-direction: column;
  color: #303030;
  font-family: MicrosoftYaHei;
}

.cn-name {
  font-size: 28px;
  font-weight: 600;
}

.en-name {
  font-size: 15px;
}

.search {
  display: flex;
  justify-content: flex-end;
  font-size: 5px;
}

.search input {
  border: 2px solid #3A5FCD;
  height: 40px;
  width: 350px;
  border-radius: 4px 0 0 4px;
  padding-left: 20px;
}

.search button {
  height: 44px;
  background-color: #3A5FCD;
  color: #FFF;
  border-radius: 0 4px 4px 0;
  line-height: 44px;
  text-align: center;
}

.navi {
	height: 60px;
	width: 100%;
	display: flex;
	margin-bottom: 20px;
}

.navi view {
	height: 100%;
	width: 13%;
	text-align: center;
	line-height: 60px;
	font-size: 20px;
	font-weight: bold;
}

.navi .a {
	background-color: #3A5FCD;
	color: #FFF;
}

.navi .b{
	color: #3A5FCD;
}

.answer {
	display: flex;
	justify-content: space-between;
}

.answer-card {
	border: 1px solid #ebeef5;
	border-radius: 4px;
	box-shadow: rgb(0 0 0 / 8%) 0px 0px 3px 1px;
	width: 780px;
	height: 170px;
}

.answer-tip {
	padding: 10px;
	padding-bottom: 20px;
	margin: 10px;
	margin-bottom: 0px;
	border-bottom: 1px #ebeef5 solid;
	font-size: 18px;
}

.answer-tip image {
	width: 23px;
	height: 23px;
	margin-right: 10px;
	vertical-align: text-bottom;
}

.answer-content {
	padding: 10px;
	margin: 10px;
	margin-bottom: 0;
}

.answer-action {
	display: flex;
	justify-content: flex-end;
	margin-bottom: 10px;
}

.answer-action-item {
	margin-right: 15px;
}

.answer-action-item image {
	width: 20px;
	height: 20px;
	vertical-align: bottom;
	margin-right: 5px;
}

#viz {
  border: 1px solid #ebeef5;
  border-radius: 4px;
  box-shadow: rgb(0 0 0 / 8%) 0px 0px 3px 1px;
  height: 400px;
  width: 400px;
}
</style>
