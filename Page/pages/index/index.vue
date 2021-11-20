<template>
    <view>
		<view class="top-title">
			<text class='title1'>合理用药智能问答平台</text>
		</view>
		<view class="englishName">
			<text class='title2'>Intelligent Q & A platform for rational drug use</text>
		</view>
		<image class="beijing" src="../../static/backGround/药品背景3.jpg" mode="aspectFill"></image>
		<!-- 介绍 -->
		<view class="text-area">
			<text class='title'>-更高效的服务，更智能的问答-</text>
		</view>
        <view class="uni-form-item uni-column">
            <input class="uni-input" focus placeholder="如果您有关于医药知识相关问题,请搜索" />
			<button>提交</button>
        </view>
    </view>
</template>

<script>
	export default {
	    data() {
	        return {
	            title: 'input',
	            focus: false,
	            inputValue: '',
	            changeValue: ''
	        }
	    },
	    methods: {
	        onKeyInput: function(event) {
	            this.inputValue = event.target.value
	        },
	        replaceInput: function(event) {
	            var value = event.target.value;
	            if (value === '11') {
	                this.changeValue = '2';
	            }
	        },
	        hideKeyboard: function(event) {
	            if (event.target.value === '123') {
	                uni.hideKeyboard();
	            }
	        }
	    }
	}
</script>

<style>
	.top-title{
		color: #00008B;
		font-size: 40px;
		font-family: Simsun;
		display: flex;
		justify-content: center;
	}
	.englishName{
		color: #4F4F4F;
		font-size: 20px;
		font-family: Simsun;
		display: flex;
		justify-content: center;
	}
	.uni-form-item{
			display: flex;
			justify-content: center;
			margin-top: 80px;
	}
	input{
		height: 40px;
		width: 300px;
		background-color: #FFFFFF;
	}
	button{
		height: 40px;
		width: 80px;
		background-color:#4876FF;
		margin: 0;
	}
	.beijing{
		height: 100%;
		width: 100%;
		position: fixed;
		top: 15;
		z-index: -1;
	}
	.text-area{
		color:#FFFFFF ;
		font-size: 40rpx;
		margin-top: 80px;
		margin-left: 30px;
	}
</style>