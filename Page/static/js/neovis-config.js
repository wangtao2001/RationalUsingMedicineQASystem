export default {
    container_id: "viz",
    server_url: "neo4j://localhost:7687",
    server_user: "neo4j",
    server_password: "qazplm-55454",
    // 结点
    labels: {
        
    },
	// 关系边
	relationships: {
		 
	},
	// 初始化语句
	initial_cypher: "match(n) return n limit 25"
};