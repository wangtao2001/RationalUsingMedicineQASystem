<template>
	<view id="app">
		<Grid :items="items" class="root-grid"></Grid>
	</view>
</template>

<script>
	import Grid from "../../components/Grid.vue"
	export default {
		components:{Grid},
		data() {
			return {
				items:[
					{
						icon:  require("../../static/dialectics/八纲辨证.png"),
						title: "八纲辨证"
					},
					{
						icon:  require("../../static/dialectics/病因辨证.png"),
						title: "病因辨证"
					},
					{
						icon:  require("../../static/dialectics/气血阴阳精髓津液辨证.png"),
						title: "气血阴阳精髓津液辨证"
					},
					{
						icon:  require("../../static/dialectics/脏腑官窍辨证.png"),
						title: "脏腑官窍辨证"
					},
					{
						icon:  require("../../static/dialectics/经络辨证.png"),
						title: "经络辨证"
					},
					{
						icon:  require("../../static/dialectics/六经辨证.png"),
						title: "六经辨证"
					},
					{
						icon:  require("../../static/dialectics/三焦辨证.png"),
						title: "三焦辨证"
					},
					{
						icon:  require("../../static/dialectics/卫气营血辨证.png"),
						title: "卫气营血辨证"
					},
					{
						icon:  require("../../static/dialectics/其他辨证.png"),
						title: "其他辨证"
					},
				
				]
			}
		}
	}
</script>

<style>
</style>

