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

  // Adicionar nós
  for (const [key, values] of Object.entries(rank)) {
    // Criar nós para cada value no rank atual
    values.forEach((value, index) => {
        const from = value[0];
        const to = value[1];
        if (!(from in nodeIds)) {
            nodeIds[from] = idCounter++;
            label = from;
            if (index == 0){
                label = "P4-enabled\n6LoWPAN (root)";
                nodes.push({
                    id: nodeIds[from],
                    label: label, // O label é o value
                    //image: DIR + "icon.png", // Escolha a imagem apropriada
                    borderWidth: 3,
                    //shape: "database",
                    color: "orange",
                    //shape: "image",
                });
            }
            else{
                nodes.push({
                    id: nodeIds[from],
                    label: label.substring(label.length - 14), // O label é o value
                    //image: DIR + "icon.png", // Escolha a imagem apropriada
                    borderWidth: 3,
                    //shape: "database",
                    //shape: "image",
                });
            }
        }

        if (!(to in nodeIds)) {
            nodeIds[to] = idCounter++;
            label = to
            nodes.push({
                id: nodeIds[to],
                label: label.substring(label.length - 14), // O label é o value
                //image: DIR + "icon.png", // Escolha a imagem apropriada
                borderWidth: 3,
                //shape: "database",
                //color: "orange",
                //shape: "image",
            });
        }

        edges.push({ from: nodeIds[from], to: nodeIds[to], color: "black", width: 1, length: EDGE_LENGTH_MAIN });
    });
    }
}

// Função principal para desenhar o grafo
function draw() {
  // Defina o IP e a porta do servidor Flask
  const serverIp = '192.168.210.1';
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
          var options = { layout: { randomSeed: 8 } };
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
