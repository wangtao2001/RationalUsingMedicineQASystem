export default {
    container_id: "viz",
    server_url: "neo4j://localhost:7687",
    server_user: "neo4j",
    server_password: "qazplm-55454",
	labels: {
		    "方剂": {
		        "caption": "方剂名称",
		        "size": "point",
		        "title_properties":[
		            "方剂名称",
		            "功效主治",
		            "药材配方",
		            "方剂用法",
		            "方剂出处"
		        ]
		    },
		    "中药": {
		        "caption": "中药名称",
		        "size": "point",
		        "title_properties": [
		            "中药名称",
		            "中药别名",
		            "中药出处",
		            "功效主治",
		            "中药种属",
		            "性味归经",
		            "形态特征",
		            "功能主治",
		            "保存方法",
		        ],
		    },
		    "方剂分类": {
		        "caption": "方剂分类名称",
		        "size": "point"
		    },
		    "美容方剂": {
		        "caption": "方剂名",
		        "size": "point",
		        "title_properties":[
		            "方剂名",
		            "配伍用量",
		            "功效",
		            "用法",
		            "来源",
		            "治法",
		            "备注"
		        ]
		    },
		    "皮肤病": {
		        "caption": "皮肤病名称",
		        "size": "point"
		    },
		    "中药分类":{
		        "caption": "中药分类名称",
		        "size": "point"
		    },
		    "证候":{
		        "caption": "证候名称",
		        "size": "point"
		    },
		    "其他治法":{
		         "caption": "其他治法名",
		        "size": "point"
		    }
		}
};