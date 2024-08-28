var nodes = null;
var edges = null;
var network = null;

var DIR = "./img/";
var EDGE_LENGTH_MAIN = 150;
var EDGE_LENGTH_SUB = 50;


//var nodes = new vis.DataSet([]);
//var edges = new vis.DataSet([]);
var isInteracting = false;
var prev_state = [];
var curr_state = [];

// Função para criar nós e arestas com base nos dados recebidos
function processData(rank) {

  nodes = [];
  edges = [];

  let idCounter = 1;
  const nodeIds = {};
  let parent = 0;

  // Adicionar nós
  for (const [key, values] of Object.entries(rank)) {
    // Criar nós para cada value no rank atual
    values.forEach(value => {
        if (!(value in nodeIds)) {
            nodeIds[value] = idCounter++;
            label = `${values.join(', ')}`
            if (key == 1)
                label = "root"
            nodes.push({
                id: nodeIds[value],
                label: label, // O label é o value
                image: DIR + "icon.png", // Escolha a imagem apropriada
                shape: "image",
            });
        }

        // Conectar nó de rank atual ao próximo rank
        const nextRankKey = String(Number(key) + 1);
        if (nextRankKey in rank) {
            const nextRankValues = rank[nextRankKey];

            // Conectar todos os values do rank atual ao próximo rank
            nextRankValues.forEach(nextValue => {
                if (!(nextValue in nodeIds)) {
                    nodeIds[nextValue] = idCounter++;
                    nodes.push({
                        id: nodeIds[nextValue],
                        label: nextValue, // O label é o próximo value
                        image: DIR + "icon.png", // Escolha a imagem apropriada
                        shape: "image",
                    });
                }

                // Conectar value atual ao próximo rank
                edges.push({ from: nodeIds[value], to: nodeIds[nextValue], length: EDGE_LENGTH_MAIN });
            });
        }
    });
    }
}

// Função principal para desenhar o grafo
function draw() {
  // Defina o IP e a porta do servidor Flask
  const serverIp = '10.0.0.1';
  const serverPort = '5000';

  // Construa a URL completa da requisição
  const url = `http://${serverIp}:${serverPort}/api`;
  // Faça a requisição para a API
  fetch(url)
    .then(response => response.json())
    .then(data => {
      processData(data);



      if (!network) {
      // Criar a rede de visualização
      var container = document.getElementById("mynetwork");
      var data = {
        nodes: nodes,
        edges: edges,
      };
      var options = {};
      network = new vis.Network(container, data, options);
      }
      else{

        network.on("dragStart", function () {
          isInteracting = true; // Define a flag quando um nó é selecionado
        });
        network.on("dragEnd", function () {
          isInteracting = false; // Define a flag quando um nó é selecionado
        });

        if (!isInteracting){
         // Atualiza a rede existente com os novos dados
        network.setData({
          nodes: nodes,
          edges: edges
        });
	}

      }
    });
}

window.addEventListener("load", () => {
  draw();
});

// Atualiza a rede a cada 1 segundo
setInterval(draw, 1000);
