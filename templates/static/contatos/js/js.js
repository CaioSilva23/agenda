$('#example').DataTable({
    paging: true, // pagination
    pageLength: 1, //data per page
    lengthChange: true, //show entries per page
    autoWidth: true, // control the auto width on columns
    searching: true, //campo de pesquisa 
    bInfo: true, // info footer
    bSort: true, // filtro A to Z and Z to A


    // Desabilitando o filtro das colunas
   //  
   // "columnDefs": [{
   //     "targets": 5, // OU UM RANGE[4,5]
   //     "orderable": false
  //  }] 

    // BOTÕES
    dom: 'lBfrtip',
    buttons: [
        { // BOTÃO DE COPIAR
        extend: 'copy',
        text: '<i class="fas fa-clone"><i/>',
        className: 'btn btn-secondary btn-sm',
        titleAttr: 'Copiar',
        // COLUNAS Q SERÁ COPIADAS
        exportOptions: {
            columns: [0, 1, 2, 3, 4, 5]
            },
        },

        { // BOTÃO DE EXPORTAR EXCEL
            extend: 'excel',
            text: '<i class="fas fa-file-excel"><i/>',
            className: 'btn btn-secondary btn-sm',
            titleAttr: 'Excel',
            // COLUNAS Q SERÁ COPIADAS
            exportOptions: {
                columns: [0, 1, 2, 3, 4, 5]
                },
            },

        { // BOTÃO DE IMPRESSAO 
            extend: 'print',
            text: '<i class="fas fa-print"><i/>',
            className: 'btn btn-secondary btn-sm',
            titleAttr: 'Imprimir',
            // COLUNAS Q SERÁ IMPRESSAS
            exportOptions: {
                columns: [0, 1, 2, 3, 4, 5]
                },
                // font da impressão 
                customize: function(win){
                    $(win.document.body).css('font-size','8pt')
                    $(win.document.body).find('table')
                    .addClass('compact')
                    .css('font-size', 'inherit');
                }
            },
        { // BOTÃO DE PDF 
            extend: 'pdf',
            text: '<i class="fas fa-file-pdf"><i/>',
            className: 'btn btn-secondary btn-sm',
            titleAttr: 'PDF',
            // COLUNAS Q SERÁ IMPRESSAS
            exportOptions: {
                columns: [0, 1, 2, 3, 4, 5]
                },
                
                // Centralizando a tabela no meio 
                tableHeader:{
                    alignment: 'center'    
                },
                // font e posicao 
                customize: function(doc){
                    doc.styles.tableHeader.alignment = 'center';
                    doc.styles.tableBodyOdd.alignment = 'center';
                    doc.styles.tableBodyEven.alignment = 'center';
                    doc.styles.tableHeader.fontSize = 9;
                    doc.defaultStyle.fontSize = 6;
                    doc.content[1].table.widths = Array(doc.content[1].table.body[1].length + 1 ).join('*').split('');
                }       
                
            },
    ]
});