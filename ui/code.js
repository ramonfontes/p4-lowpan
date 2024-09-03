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

var packet_size_nodes = [];

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

function processPacketSize(data) {
  const tabelaBody = document.querySelector('#packet_size tbody');

  for (const [key, value] of Object.entries(data)) {
        let existingRow = Array.from(tabelaBody.rows).find(row => row.cells[0].textContent === key);

        if (existingRow) {
            existingRow.cells[1].textContent = value  + " Bytes";
        }
        else{
            // Criando uma nova linha
            const row = document.createElement('tr');

            // Criando e adicionando as células na linha
            const cellId = document.createElement('td');
            cellId.textContent = key;
            row.appendChild(cellId);

            const cellNome = document.createElement('td');
            cellNome.textContent = value + " Bytes";
            row.appendChild(cellNome);

            // Adicionando a linha na tabela
            tabelaBody.appendChild(row);
        }
  }
}

function exportToSVG() {
  const container = document.getElementById("mynetwork");

  domtoimage.toSvg(container)
    .then(function (dataUrl) {
      // Create a link element to download the SVG
      var link = document.createElement('a');
      link.href = dataUrl;
      link.download = 'network-visualization.svg';
      link.click();
    })
    .catch(function (error) {
      console.error('Oops, something went wrong!', error);
    });
}

document.getElementById("exportButton").addEventListener("click", exportToSVG);

// Função principal para desenhar o grafo
function draw() {
  // Defina o IP e a porta do servidor Flask
  const serverIp = '10.0.0.1';
  const serverPort = '5000';

  // Construa a URL completa da requisição
  const url = `http://${serverIp}:${serverPort}/api`;
  const url_packet_size = `http://${serverIp}:${serverPort}/api/packet_size`;
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

    fetch(url_packet_size)
    .then(response => response.json())
    .then(data => {
      processPacketSize(data);
    });
}

window.addEventListener("load", () => {
  draw();
});

// Atualiza a rede a cada 1 segundo
setInterval(draw, 1000);