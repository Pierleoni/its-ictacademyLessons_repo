 
<%*
const input = await tp.user.numberInput();


function conversione(input) {
    let procedura = "";

    // If the input is a binary number
    if (/^[01]+$/.test(input)) {
        const decimale = parseInt(input, 2); // Conversion to decimal
        procedura += `**Conversione Binario -> Decimale**:\n`;
        procedura += `1. Ogni cifra binaria rappresenta una potenza di 2, partendo da destra.\n`;
        procedura += `   ${input.split("").reverse().map((bit, i) => `${bit} × 2^${i}`).join(" + ")} = ${decimale}\n`;
        procedura += `\n**Risultato:** ${input} (binario) = ${decimale} (decimale)\n`;
    } 
    // If the input is a decimal number
    else if (/^\d+$/.test(input)) {
        const numero = parseInt(input);
        const binario = numero.toString(2); // Conversion to binary
        procedura += `**Conversione Decimale -> Binario**:\n`;
        procedura += `1. Dividi il numero per 2 e annota i resti:\n`;

        let n = numero;
        let passaggi = [];
        while (n > 0) {
            const resto = n % 2;
            passaggi.push(`${n} ÷ 2 = ${Math.floor(n / 2)} con resto ${resto}`);
            n = Math.floor(n / 2);
        }
        procedura += passaggi.join("\n") + "\n";
        procedura += `2. Leggi i resti dal basso verso l'alto: ${binario}\n`;
        procedura += `\n**Risultato:** ${numero} (decimale) = ${binario} (binario)\n`;
    } 
    // If the input is invalid
    else {
        procedura = "L'input non è valido. Inserisci un numero decimale o una sequenza binaria.";
    }

    return procedura;
}

const risultato = conversione(input.trim());
%>
<%= risultato %>




