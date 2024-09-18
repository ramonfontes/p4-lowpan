var nodes = null;
var edges = null;
var network = null;
var alertShown = false;
var isConnected = false;
var isInteracting = false;
var EDGE_LENGTH_MAIN = 150;
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
                    label: label,
                    borderWidth: 3,
                    color: "orange",
                });
            }
            else{
                nodes.push({
                    id: nodeIds[from],
                    label: label.substring(label.length - 14),
                    borderWidth: 3,
                });
            }
        }

        if (!(to in nodeIds)) {
            nodeIds[to] = idCounter++;
            label = to
            nodes.push({
                id: nodeIds[to],
                label: label.substring(label.length - 14),
                borderWidth: 3,
            });
        }

        edges.push({ from: nodeIds[from], to: nodeIds[to], color: "black", width: 1, length: EDGE_LENGTH_MAIN });
    });
  }
}

function handleError(error) {
    console.error("An error occurred:", error);
    if (!alertShown) {
        alert("An error occurred:", error);
        alertShown = true;  // Marcar que o alerta já foi mostrado
    }
}

function handleOffline() {
    if (!alertShown) {
        alert("The system is offline");
        alertShown = true;  // Marcar que o alerta já foi mostrado
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

        const rowsArray = Array.from(tabelaBody.rows);

        rowsArray.sort((rowA, rowB) => {
            const textA = rowA.cells[0].textContent.trim().replace(/[^0-9.]/g, '');
            const textB = rowB.cells[0].textContent.trim().replace(/[^0-9.]/g, '');

            // Converte para números para comparação
            const numA = parseFloat(textA);
            const numB = parseFloat(textB);

            // Ordena numericamente
            return numA - numB;
        });

        // Remove todas as linhas do tbody
        while (tabelaBody.firstChild) {
            tabelaBody.removeChild(tabelaBody.firstChild);
        }
        console.log(rowsArray);
        // Adiciona as linhas ordenadas de volta ao tbody
        rowsArray.forEach(row => tabelaBody.appendChild(row));
    }
  }
}

// Função principal para desenhar o grafo
async function draw() {
  // Defina o IP e a porta do servidor Flask
  const serverIp = '192.168.210.1';
  const serverPort = '5000';

  // Construa a URL completa da requisição
  const url = `http://${serverIp}:${serverPort}/api`;
  const url_packet_size = `http://${serverIp}:${serverPort}/api/packet_size`;

  const controller = new AbortController();
  const signal = controller.signal;
  timeout = 1000;

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

    await fetch(url_packet_size, { signal })
    .then(response => {
        if (!response.ok) {
            handleError;
        }
        return response.json();
    })
    .then(data => {
        processPacketSize(data);
    })
    .catch(handleError);

    if (!isConnected){
        nodes = null;
        edges = null;
        if (network)
            network.setData({
                nodes: nodes,
                edges: edges
            });
        const tabelaBody = document.querySelector('#packet_size tbody');
        // Limpar o conteúdo do <tbody>
        tabelaBody.innerHTML = '';
        isConnected = true;
        alertShown = false;
        handleOffline();
    }
}

window.addEventListener("load", () => {
  draw();
});

// Atualiza a rede a cada 1 segundo
setInterval(draw, 1000);
