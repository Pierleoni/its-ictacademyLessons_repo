


# Introduzione: Usare lo Stack Navigator con Expo Router

Lo Stack è:
- ==uno dei principali strumenti di navigazione che permette di spostarci tra le schermate sui dispositivi mobili.== 
In questa lezione impareremo come navigare e trasferire dati tra le schermate all'interno di uno stack.

Nelle sezioni precedenti abbiamo costruito le fondamenta: 
sappiamo come [[Lezione 1 - Introduzione a EXPO SDK 55 e Navigazione#Percorsi e cartelle|strutturare le route con file e cartelle]], come [[Lezione 1 - Introduzione a EXPO SDK 55 e Navigazione#Schermate e file di Layout|i layout si annidano]] e [[Lezione 1 - Introduzione a EXPO SDK 55 e Navigazione#Ordine di esecuzione dei file di `_layout`|si eseguono dall'esterno verso l'interno]], come [[Lezione 1 - Introduzione a EXPO SDK 55 e Navigazione#Linking tra le schermate|`<Link>`]] e [[Lezione 1 - Introduzione a EXPO SDK 55 e Navigazione#`useRouter()`|`useRouter()`]] permettono di navigare tra le schermate, e come lo [[Lezione 1 - Introduzione a EXPO SDK 55 e Navigazione#^752b8b|`<Stack />`]] mantiene [[Lezione 1 - Introduzione a EXPO SDK 55 e Navigazione#Lo stack di navigazione|la pila delle schermate visitate]].

Tuttavia fino ad ora abbiamo usato lo `<Stack />` in modo minimale — lo abbiamo dichiarato nel root layout e lasciato fare il suo lavoro in modo automatico. Nella pratica, lo Stack navigator è molto più potente e configurabile di così.

In questa lezione lo esploriamo in profondità. Partiremo dalla navigazione di base per poi affrontare scenari più complessi:

- **[[#Navigazione in uno stack|Navigazione in uno stack]]** — come funziona la pila nel dettaglio e come controllarla
- **[[#Ritorno a una schermata esistente|Ritorno a una schermata già esistente]]** — cosa succede quando la schermata di destinazione è già presente nello stack
- **[[#Sostituzione della schermata corrente|Sostituzione della schermata corrente]]** — quando e come usare `replace` in modo consapevole
- **[[#L'opzione di navigazione|Opzioni di navigazione]]** — come configurare le transizioni e il comportamento dello stack
- **[[#Passaggio di Parametri tra le schermate|Passaggio di parametri tra le schermate]]** — come mandare dati da una schermata all'altra durante la navigazione
- **[[#Percorsi dinamici|Percorsi dinamici]]** — come creare route parametriche che si adattano ai dati, come `/products/[id]`
- **[[#Rotte dinamiche annidate|Percorsi dinamici annidati]]** — come gestire route dinamiche a più livelli di profondità
- **[[#Opzioni Schermata|Opzioni di schermata]]** — come personalizzare header, titolo e stile di ogni singola schermata

## Navigazione in uno stack 

Per esplorare il comportamento dello stack in dettaglio, riportiamo il progetto a una struttura semplice: un unico `_layout.tsx` con uno `<Stack />` e quattro schermate collegate tra loro.

`src/app/index.tsx` — schermata di partenza con link a tutte le altre:
```tsx
import { Link, useRouter } from "expo-router";
import { View, Text, StyleSheet, Pressable, Button } from "react-native";

export default function HomeScreen() {
  const router = useRouter();

  return (
    <View style={styles.container}>
      <Text style={styles.heading}>Index Screen</Text>

      <Link href="/secondIndex" push asChild>
        <Pressable style={styles.button}>
          <Text>Push to second</Text>
        </Pressable>
      </Link>

      <Link href='/third' push asChild>
        <Button title="Push to Third" />
      </Link>

      <Pressable style={styles.button} onPress={() => router.push("/fourthIndex")}>
        <Text style={styles.textBtn}>Push to fourth (imperativo)</Text>
      </Pressable>

      <Link href='/fourthIndex' push asChild>
        <Pressable style={styles.button}>
          <Text>Push to fourth</Text>
        </Pressable>
      </Link>
    </View>
  );
}
```

`src/app/secondIndex.tsx` — sfondo blu per riconoscerla facilmente:
```tsx
export default function SecondIndex() {
  return (
    <View style={styles.container}>
      <Text style={styles.heading}>Second Screen</Text>
      <Link href='/third' push asChild>
        <Button title="Push to Third" />
      </Link>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    padding: 16,
    backgroundColor: 'rgba(19, 29, 216, 1)',
  },
  heading: {
    fontSize: 24,
    fontWeight: "bold",
    textAlign: "center",
  },
});
```

`src/app/third.tsx` — sfondo verde:
```tsx
export default function ThirdIndex() {
  return (
    <View style={styles.container}>
      <Text style={styles.heading}>Third Screen</Text>
      <Link href='/' push asChild>
        <Button title="Ritorna all'indice" />
      </Link>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    padding: 16,
    backgroundColor: 'rgba(40, 193, 45, 1)',
  },
  heading: {
    fontSize: 24,
    fontWeight: "bold",
    textAlign: "center",
  },
});
```

#### Il problema del `push` infinito

Tutti i collegamenti sono impostati su `push` — ogni navigazione aggiunge una nuova schermata allo stack. Navigando Index → Second → Third → Index → Second → Third, lo stack cresce indefinitamente:
```txt
STACK dopo la prima passata:
┌─────────┐
│  Third  │
├─────────┤
│ Second  │
├─────────┤
│  Index  │
└─────────┘

STACK dopo la seconda passata:
┌─────────┐
│  Third  │
├─────────┤
│ Second  │
├─────────┤
│  Index  │  ← secondo giro
├─────────┤
│  Third  │
├─────────┤
│ Second  │
├─────────┤
│  Index  │  ← primo giro
└─────────┘
```

Quando si preme "indietro", si percorre lo stack al contrario — si risalgono tutte le schermate accumulate, una per una, nell'ordine inverso in cui sono state visitate.

Togliendo `push` dal link "Ritorna all'indice" in `third.tsx`, il comportamento diventa `replace` — Index **sostituisce** Third invece di accumularsi sopra:
```txt
STACK con replace su "Ritorna all'indice":
┌─────────┐
│  Index  │  ← sostituisce Third
├─────────┤
│ Second  │
├─────────┤
│  Index  │
└─────────┘
↓ premi indietro 2 volte per tornare alla root
```

> [!warning] **`push` non è sempre la scelta giusta** 
>  ==Usare `push` per navigare verso schermate che fanno parte di un flusso ciclico (es. A → B → A → B) accumula schermate nello stack senza limite.== 
>  **L'utente si ritrova a dover premere "indietro" molte più volte del previsto.**

>[!info]  **`replace` non "torna" — ricrea** `replace` non ripristina la schermata precedente — **crea una nuova istanza** della schermata di destinazione che sostituisce quella corrente.
>**Dimostrazione pratica** — aggiungiamo un counter a `index.tsx`:
>```tsx
>const [count, setCount] = useState<number>(0);
>
><Pressable onPress={() => setCount(prev => prev + 1)}>
>  <Text>+</Text>
></Pressable>
><Pressable onPress={() => setCount(prev => prev - 1)}>
>  <Text>-</Text>
></Pressable>
><Text>{count}</Text>
>```
>
>Incrementa il counter, naviga verso Second con `push`, poi premi "Ritorna all'indice" da Third con `replace` — il counter torna a `0`.
>
>`replace` non ha ripristinato lo stato precedente — ha creato una **nuova istanza** di Index con lo stato azzerato. Se fosse stato un `push` seguito da un `back()`, lo stato sarebbe rimasto invariato perché la schermata originale sarebbe ancora nello stack.

> [!tip] **Quando usare `replace` invece di `push`** 
> Se la navigazione è ciclica o non ha senso tornare indietro alla schermata precedente, usa `replace` — sostituisce la schermata corrente senza accumularla nello stack:
>```tsx
> // invece di push che accumula
><Link href='/third' push asChild>
>
>// replace che non accumula
><Link href='/third' asChild>  {/* replace è il default */}
>```

### Ritorno a una schermata esistente  
Finora abbiamo visto [[Lezione 1 - Introduzione a EXPO SDK 55 e Navigazione#^30f337|`push`]] e [[Lezione 1 - Introduzione a EXPO SDK 55 e Navigazione#^replace|`replace`]] — ma esiste una terza opzione per la navigazione: **`dismissTo`.**
Questa prop di `<Link>`: 
- ==non crea una nuova istanza della schermata di destinazione,== 
- **né sostituisce quella corrente:**
	- ==cerca nello stack **un'istanza già esistente** della route e fa pop di tutte le schermate sopra fino a raggiungerla.==
```tsx
export default function ThirdIndex() {
  const router = useRouter();

  return (
    <View style={styles.container}>
      <Text style={styles.heading}>Third Index Screen</Text>

      {/* replace — crea nuova istanza di Index */}
      <Link href='/' asChild style={styles.button}>
        <Button title="Ritorna all'indice (replace)" />
      </Link>

      {/* dismissTo — torna all'istanza già nello stack */}
      <Link href='/' dismissTo asChild>
        <Button title="Dismiss to Index" />
      </Link>
    </View>
  );
}
```

#### Come funziona `dismissTo`

**Scenario 1 — Index è presente una sola volta nello stack:**
Partiamo dalla situazione più semplice: 
- navighiamo Index → Second → Third.
Lo stack contiene tre schermate e Index si trova in fondo:
```
STACK: [ Index, Second, Third ]
→ dismissTo '/'
→ trova Index in fondo → pop di Third e Second
STACK: [ Index ] ✅ — unica schermata, niente freccia indietro
```
`dismissTo` risale lo stack, trova l'unica istanza di Index e fa pop di tutte le schermate sopra in un colpo solo. Il risultato è uno stack con una sola schermata — niente freccia indietro.
```tsx
// index.tsx
<Link href="/secondIndex" push asChild>
  <Pressable style={styles.button}>
    <Text>Push to second</Text>
  </Pressable>
</Link>

// secondIndex.tsx
<Link href='/third' push asChild>
  <Button title="Push to Third" />
</Link>

// third.tsx
<Link href='/' dismissTo asChild>
  <Button title="Dismiss to Index" />
</Link>
```

```txt
STACK prima del dismissTo:
┌─────────┐
│  Third  │  ← schermata corrente
├─────────┤
│ Second  │
├─────────┤
│  Index  │  ← unica istanza
└─────────┘

→ dismissTo '/'
→ trova Index in fondo → pop di Third e Second

STACK dopo il dismissTo:
┌─────────┐
│  Index  │  ✅ unica schermata, niente freccia indietro
└─────────┘

```
`dismissTo` risale lo stack, trova l'unica istanza di Index e fa pop di tutte le schermate sopra in un colpo solo.


**Scenario 2 — Index è presente più volte nello stack (due giri):**

Per ottenere questo scenario tutti i link devono usare `push` — incluso quello da Third verso Index:
```
Navigazione: Index → Second → Third → Index → Second → Third

STACK: [ Index, Second, Third, Index, Second, Third ]
→ dismissTo '/'
→ trova l'istanza di Index più in alto → pop di Third e Second sopra di essa
STACK: [ Index, Second, Third, Index ] ← freccia indietro ancora visibile ✅
```
Qui `dismissTo` non risale fino alla root — si ferma alla **prima istanza di Index che trova partendo dall'alto**. Fa pop solo di Third e Second del secondo giro, lasciando intatto tutto quello sotto. Per questo la freccia indietro è ancora visibile — ci sono ancora schermate sotto nello stack.
```tsx
// index.tsx
<Link href="/secondIndex" push asChild>
  <Pressable style={styles.button}>
    <Text>Push to second</Text>
  </Pressable>
</Link>

// secondIndex.tsx
<Link href='/third' push asChild>
  <Button title="Push to Third" />
</Link>

// third.tsx — link replace verso Index (default) per tornare e ripartire
<Link href='/' asChild style={styles.button}>
  <Button title="Ritorna all'indice (replace)" />
</Link>

// third.tsx — dismissTo per lo scenario
<Link href='/' dismissTo asChild>
  <Button title="Dismiss to Index" />
</Link>
```
Sequenza di navigazione: `Index → Second → Third → **replace** → Index → Second → Third.`

Usando `replace` da Third verso Index, Index sostituisce Third nello stack — e poi facendo push di nuovo verso Second e Third, otteniamo:
```txt
STACK prima del dismissTo:
┌─────────┐
│  Third  │  ← schermata corrente (secondo giro)
├─────────┤
│ Second  │  ← secondo giro
├─────────┤
│  Index  │  ← secondo giro (replace ha sostituito il primo Third)
├─────────┤
│ Second  │  ← primo giro
├─────────┤
│  Index  │  ← originale
└─────────┘

→ dismissTo '/'
→ trova l'istanza di Index più in alto → pop di Third e Second del secondo giro

STACK dopo il dismissTo:
┌─────────┐
│  Index  │  ← secondo giro
├─────────┤
│ Second  │  ← primo giro
├─────────┤
│  Index  │  ← originale
└─────────┘
↓ freccia indietro ancora visibile ✅
```

`dismissTo`: ==si ferma alla prima istanza di Index che trova partendo dall'alto — non risale fino alla root==. 
Per questo la freccia indietro è ancora visibile — ci sono ancora schermate sotto nello stack.
>[!faq] **Perché si ferma all'Index più in alto e non a quello originale?** 
>`dismissTo` **funziona come una ricerca dall'alto verso il basso** — ==appena trova la prima corrispondenza si ferma==. 
>==Non sa quante istanze della stessa route ci sono nello stack.== 
>>[!info] **Se vuoi svuotare completamente lo stack e tornare alla root, dovresti usare `router.dismissAll()` — che vedremo più avanti.**



>[!difference] **Confronto tra i tre approcci**
> `push` → ==aggiunge una nuova schermata sopra allo stack== 
> `replace` → ==sostituisce la schermata corrente con una nuova istanza== 
> `dismissTo` → ==fa pop fino all'istanza già esistente nello stack==
>>[!remember]
>>- Usa `push` ==per navigazione in avanti==
>>- Usa `replace` ==quando non ha senso tornare indietro (es. dopo il login)==
>>- Usa `dismissTo` ==quando vuoi tornare a una schermata già visitata senza ricrearla==

>[!warning] **`dismissTo` vs `back()`**
>
>- `back()` ==fa pop di **una sola schermata** alla volta==
>- `dismissTo` ==fa pop di **tutte le schermate** fino alla destinazione in un solo colpo==


### Sostituzione della schermata corrente 
Abbiamo come ritornare alla schermata precedente tramite `dismissTo`, un altra prop per il componente `<Link></Link>` è `replace`: 
- non _aggiunge_ una nuova schermata allo stack: 
	- ==**sostituisce la schermata corrente** con quella di destinazione, eliminandola dallo storico.==
#### Esempio pratico del tutorial
Partendo da questo stack:
```
[ index ] → [ second ] → [ third ]  ← (schermata corrente)
```

Premendo "Replace with /secondIndex" dalla schermata `third`:
```
[ index ] → [ second ] → [ second ]  ← (third è stata sostituita)
```

Il risultato è che: 
- ==ora abbiamo **due istanze di `second`** nello stack.== 
- ==Il pulsante Back sulla nuova `second` riporta alla `second` precedente, perché `third` è stata eliminata dallo storico e al suo posto è stata inserita la nuova schermata.== 
Premendo Back due volte:
```
Back → second (istanza precedente)
Back → index
```

Nel codice di `third.tsx`: 
```tsx
<Link href='/secondIndex' replace asChild>
  <Button title="Replace with /secondIndex" />
</Link>
```


> [!info] Il prop `replace` su `Link` è equivalente a:
>```tsx
> router.replace('/secondIndex')
>```

##### Differenza chiave rispetto a `push`

|Comportamento|Stack risultante|
|---|---|
|`push('/second')` da `third`|`index → second → third → second`|
|`replace('/second')` da `third`|`index → second → second`|

Con `push`, `third` ==resta nello stack e l'utente può tornarci.== 
Con `replace`, ==`third` sparisce definitivamente e viene sostituita dalla nuova schermata.==

#### Quando usare `replace`

Il caso più comune è la navigazione post-login: sostituendo la schermata di login con la home, il pulsante Back non potrà mai riportare l'utente al form di accesso.

```tsx
// app/login.tsx
export default function Login() {
  const router = useRouter();

  const handleLogin = async () => {
    await authenticateUser(); // chiamata API
    // replace invece di push: l'utente non potrà tornare al login con Back
    router.replace('/home');
  };

  return (
    <View>
      <TextInput placeholder="Email" />
      <TextInput placeholder="Password" secureTextEntry />
      <Button title="Accedi" onPress={handleLogin} />
    </View>
  );
}
```

- Con `push('/home')`: 
	- ==lo stack sarebbe `[ login ] → [ home ]`, e premendo Back l'utente tornerebbe al form di accesso.== 
- Con `replace('/home')`: invece lo stack diventa semplicemente `[ home ]`: 
	- ==la schermata di login è stata eliminata dallo storico e il pulsante Back non ha più nulla a cui tornare.==
### L'opzione di navigazione 
Tutte le opzioni viste finora ([[Lezione 1 - Introduzione a EXPO SDK 55 e Navigazione#^30f337|`push`]], [[Lezione 1 - Introduzione a EXPO SDK 55 e Navigazione#^replace|`replace`]], [[#Come funziona `dismissTo`|`dismissTo`]]) sono disponibili anche tramite l'[[Lezione 3 - Hooks#Cosa sono gli Hooks|hook]] [[Lezione 1 - Introduzione a EXPO SDK 55 e Navigazione#`useRouter()`|`useRouter()`]], non solo come [[Lezione 2 - Il Props Object#Il Props Object|prop]] di `<Link>`.

Un'opzione di cui non abbiamo ancora parlato è `navigate`, che è anche il **comportamento predefinito di `<Link>`** quando non si specifica nessuna prop.

##### Comportamento storico (prima di SDK 52 / React Navigation 7)

In passato `navigate()` funzionava in modo ibrido: 
- ==se la schermata di destinazione **non esisteva** nello stack si comportava come [[Lezione 1 - Introduzione a EXPO SDK 55 e Navigazione#^30f337|`push`]],== 
- ==se invece **esisteva già** chiudeva tutte le schermate sopra di essa per tornare a quell'istanza.==

Quindi, partendo da `[ index ] → [ second ] → [ third ]`, chiamando `navigate('/index')` si otteneva `[ index ]`, eliminando `second` e `third` dallo stack.

##### Comportamento attuale (SDK 52+ / React Navigation 7)

Con React Navigation 7 questo comportamento è cambiato: 
- ==`navigate` è diventato essenzialmente uguale a [[Lezione 1 - Introduzione a EXPO SDK 55 e Navigazione#^30f337|`push`]], aggiungendo sempre una nuova istanza allo stack indipendentemente da quelle già esistenti.== 
E siccome Expo Router è basato su React Navigation, quindi ha ereditato questa modifica.

> [!remember] Da ricordare
> 
> 
> - ==Si può usare `navigate` al posto di `push` senza problemi==
> - Bisogna però tenere presente queste differenze di comportamento a seconda della versione del router in uso

#### Esempi pratici
`router.navigate()` vs `router.push()` — comportamento identico in SDK 52+

```
// questi due oggi si comportano allo stesso modo
router.navigate('/second');
router.push('/second');
```

Tutti i metodi disponibili tramite `useRouter()`
```tsx
const router = useRouter();

router.push('/second');        // aggiunge sempre una nuova istanza
router.replace('/second');     // sostituisce la schermata corrente
router.navigate('/second');    // come push in SDK 52+
router.back();      // torna alla schermata precedente nello stack
router.dismiss();       // chiude la schermata corrente (modale)
router.dismissTo('/index');  // torna alla prima istanza esistente di /index
```

In SDK 52+ premendo "`Push Third`" e "`Navigate Third`" otterrai lo stesso risultato: una nuova istanza di `third` aggiunta allo stack. La differenza la vedresti solo su versioni precedenti del SDK.

**Esempio concreto — `fifth.tsx`**
```tsx
import { Button, StyleSheet, Text, View } from 'react-native';
import React from 'react';
import { useRouter } from 'expo-router';

const Fifth = () => {
    const router = useRouter();
    return (
        <View style={styles.container}>
            <Text style={styles.header}>Fifth Screen</Text>
            <Button title='Push third' onPress={() => router.push('/third')} />
            <Button title='Navigate second' onPress={() => router.navigate('/secondIndex')} />
            <Button title='Replace con fourth' onPress={() => router.replace('/fourthIndex')} />
            <Button title='Back to the Index' onPress={() => router.back()} />
        </View>
    );
};
```

In SDK 52+ premendo "`Push Third`" e "`Navigate Third`" otterrai lo stesso risultato: una nuova istanza di `third` aggiunta allo stack. La differenza la vedresti solo su versioni precedenti del SDK.

### Passaggio di Parametri tra le schermate

Vediamo come passare dati da una schermata all'altra durante la navigazione.

L'attributo `href` del componente `<Link>` accetta sia una stringa che un oggetto. Quando si usa la forma a oggetto, oltre al `pathname` si può specificare anche `params`, che deve essere un **oggetto serializzabile** — non è quindi possibile passare funzioni.

```tsx
export default function HomeScreen() {

  return (

    <View style={styles.container}>

      <Text style={styles.heading}>Index Screen</Text>

  
  

      <Link href="/secondIndex" push asChild>

        <Pressable style={styles.button} >

          <Text>Push to second</Text>

  

        </Pressable>

      </Link>


      <Pressable style={styles.button} onPress={() => {

        router.push("/fourthIndex")

      }}>

        <Text style={styles.textBtn}>Push to third</Text>

      </Pressable>

      <Link href='/fourthIndex' push asChild>

        <Pressable style={styles.button} >

          <Text>Push to fourth</Text>

        </Pressable>

      </Link>

  

      <Pressable style={styles.button} onPress={() => { router.push('/fifth') }}>

        <Text>Push to fifth</Text>

      </Pressable>


      <Link href={{ pathname: '/secondIndex', params: { name: 'Marco' } }} push asChild>

        <Button title="Push another time to /secondIndex" color='#1c3ed3c8' />

      </Link>

    </View>

  );

}
```

##### Leggere i parametri con `useLocalSearchParams`

Nella schermata di destinazione si usa l'hook `useLocalSearchParams` per accedere ai parametri ricevuti. 
Con TypeScript è possibile anche tipizzarli direttamente:
```tsx
const params = useLocalSearchParams<{ name: string }>();
```

Dopodiché si può usare il valore per mostrare contenuto condizionale, come un messaggio di benvenuto:
```tsx
export default function SecondIndex() {
  const params = useLocalSearchParams<{ name: string }>();

  return (
    <View style={styles.container}>
      <Text style={styles.heading}>Second Index Screen</Text>
      {params.name ? (
        <Text>Hello <Text style={{ fontWeight: 'bold' }}>{params.name}!</Text></Text>
      ) : null}
    </View>
  );
}
```

Se il parametro `name` ==è presente viene visualizzato il messaggio di benvenuto, altrimenti non viene renderizzato nulla.==

##### `useLocalSearchParams`

 È un [[Lezione 3 - Hooks#Cosa sono gli Hooks|hook]] che permette di ==**leggere i parametri passati durante la navigazione** nella schermata corrente.== 
 "Local" significa che: 
 - ==legge solo i parametri della schermata corrente, ignorando quelli di schermate parent nella gerarchia di navigazione.==

Quando navighi verso `/secondIndex` passando `{ name: 'Marco' }`, **quei dati finiscono nella URL come query string: `/secondIndex?name=Marco`.** ==`useLocalSearchParams` non fa altro che leggere quella query string e restituirtela come oggetto.==

Con TypeScript puoi tiparla per avere l'auto-complete e la sicurezza dei tipi:
```tsx
const params = useLocalSearchParams<{ name: string }>();
// params.name → string | undefined
```

==È `undefined` se il parametro non è stato passato, per questo nel tutorial si controlla `params.name ?` prima di renderizzare il messaggio.==


##### Passare parametri tramite `useRouter`

Lo stesso comportamento si ottiene con `useRouter()`: 
- ==tutte le funzioni di navigazione come `push`, `replace` e `navigate` accettano un oggetto al posto della stringa:==
```tsx
export default function HomeScreen() {
  const router = useRouter()

  return (

    <View style={styles.container}>

      <Text style={styles.heading}>Index Screen</Text>

      <Link href="/secondIndex" push asChild>

        <Pressable style={styles.button} >

          <Text>Push to second</Text>

        </Pressable>

      </Link>

      <Pressable style={styles.button} onPress={() => {

        router.push("/fourthIndex")

      }}>

        <Text style={styles.textBtn}>Push to third</Text>

      </Pressable>

      <Link href='/fourthIndex' push asChild>

        <Pressable style={styles.button} >

          <Text>Push to fourth</Text>

        </Pressable>

      </Link>

      <Pressable style={styles.button} onPress={() => { router.push('/fifth') }}>

        <Text>Push to fifth</Text>

      </Pressable>

      <Link href={{ pathname: '/secondIndex', params: { name: 'Marco' } }} push asChild>

        <Button title="Push another time to /secondIndex" color='#1c3ed3c8' />

      </Link>

      <Button title="Another greeting message" color='#1c3ed3c8' onPress={() => router.push({ pathname: '/secondIndex', params: { name: 'Mary' } })} />

    </View>

  );

}
```
Questo rende il passaggio di parametri uniforme sia che si usi `<Link>` che l'hook `useRouter`.


#### `useLocalSearchParams` vs `useRouter`

Sono due hook con scopi completamente diversi, non sono in competizione tra loro:

- `useLocalSearchParams` ==serve per **leggere** i parametri in entrata nella schermata corrente==
- `useRouter` ==serve per **navigare** verso altre schermate, eventualmente passando parametri in uscita==

In pratica li userai spesso **insieme** sulla stessa schermata:
```tsx
export default function SecondIndex() {
  // leggo i parametri ricevuti
  const params = useLocalSearchParams<{ name: string }>();
  // mi preparo a navigare altrove
  const router = useRouter();

  return (
    <View>
      <Text>Ciao {params.name}!</Text>
      <Button title="Vai a Third" onPress={() => router.push('/third')} />
    </View>
  );
}
```

#### Quando usare `<Link>` vs `useRouter`

Questa invece è una scelta più pratica:

|                                                                                                | `<Link>`      | `useRouter`   |
| ---------------------------------------------------------------------------------------------- | ------------- | ------------- |
| Navigazione semplice                                                                           | ✅ preferibile | va bene       |
| Navigazione condizionale                                                                       | ❌ difficile   | ✅ preferibile |
| Navigazione dopo una chiamata [[Lezione 6 - API#API (Application Programming Interface)\|API]] | ❌ non adatto  | ✅ unico modo  |
| Dentro un `onPress` o evento custom                                                            | ❌ non adatto  | ✅ unico modo  |
Quindi: 
1. `<Link>` ==è comodo quando la navigazione è diretta e dichiarativa==, 

> [!example] **ad esempio un pulsante che porta sempre alla stessa schermata.**

2. `useRouter` ==è necessario quando la navigazione dipende da logica==, 

> [!example] **come navigare verso una schermata diversa in base al risultato di un login.**



### Percorsi dinamici 


Fino ad ora i percorsi erano tutti statici: `/second`, `/third`, ecc. 
Expo Router permette di: 
- ==rendere **dinamico un segmento del percorso** racchiudendolo tra parentesi quadre nel nome del file.==

Ad esempio, per una schermata che mostra un proverbio in base all'ID, si crea una cartella `proverbs/` con un file chiamato `[id].tsx`. 
**Quel segmento tra parentesi quadre diventa una variabile che cambia a seconda del percorso visitato:** ==`/proverbs/1`, `/proverbs/2`, ecc. — tutte puntano allo stesso file, ma con un `id` diverso.==

Non è necessario aggiungere un [[Lezione 1 - Introduzione a EXPO SDK 55 e Navigazione#`_layout.tsx`|`_layout.tsx`]] dentro la cartella se si vuole che la schermata continui ad essere gestita dallo Stack del layout radice.
Generiamo alcuni dati per questo file : un elenco di 10 citazioni motivazionali
```tsx
type Proverb = {

    id: string;

    proverb: string;

    source: string;

};

  

const proverbs: Proverb[] = [

    { id: "1", proverb: "Il momento migliore per piantare un albero era 20 anni fa. Il secondo momento migliore è adesso.", source: "Proverbio Cinese" },

    { id: "2", proverb: "Non importa quanto vai piano, l'importante è non fermarsi.", source: "Confucio" },

    { id: "3", proverb: "Il successo non è definitivo, il fallimento non è fatale: ciò che conta è il coraggio di andare avanti.", source: "Winston Churchill" },

    { id: "4", proverb: "Credi di potercela fare e sarai già a metà strada.", source: "Theodore Roosevelt" },

    { id: "5", proverb: "L'unico modo per fare un ottimo lavoro è amare quello che fai.", source: "Steve Jobs" },

    { id: "6", proverb: "Sii il cambiamento che vuoi vedere nel mondo.", source: "Mahatma Gandhi" },

    { id: "7", proverb: "Non hai bisogno di vedere l'intera scalinata, inizia semplicemente a salire il primo gradino.", source: "Martin Luther King Jr." },

    { id: "8", proverb: "La logica ti porterà da A a B. L'immaginazione ti porterà dappertutto.", source: "Albert Einstein" },

    { id: "9", proverb: "Il tuo tempo è limitato, quindi non sprecarlo vivendo la vita di qualcun altro.", source: "Steve Jobs" },

    { id: "10", proverb: "Cadi sette volte, rialzati otto.", source: "Proverbio Giapponese" }

];
```

**Analisi del codice:**
Con [[Lezione 4 - Array, Custom Types e Generic#Object Types|`type`]] stai definendo una **forma:**
- stai dicendo a TypeScript: =="ogni oggetto di tipo `Proverb` deve avere esattamente questi tre campi, tutti di tipo `string`".== 
- ==Non stai creando nessun dato, stai solo descrivendo la struttura che i dati dovranno rispettare.==
Con `const proverbs: Proverb[] = [ ... ]`: 
- Qui dichiari una costante `proverbs` e la tipizzi come `Proverb[]`, ovvero un **array di oggetti** che rispettano la forma descritta dal type. 
- Il `[]` dopo il tipo è la sintassi di TypeScript per dire "array di".

> [!fail] Se provassi ad aggiungere un campo extra o a ometterne uno, TypeScript ti segnalerebbe un errore a compile time — è esattamente il vantaggio di tipizzare l'array.
> 
> 

Ogni elemento dentro l'array è un oggetto letterale con le tre chiavi dichiarate nel type:
```tsx
{ id: "1", proverb: "Il momento migliore...", source: "Proverbio Cinese" }
```
##### Leggere il segmento dinamico

==Per accedere al valore dell'`id` si usa [[#`useLocalSearchParams`|`useLocalSearchParams`]], esattamente come per i parametri passati manualmente.== 
Expo Router tratta i segmenti dinamici come parametri:
```tsx
// dichiaro hooks che legge solo i parametri della schermata corrente
// in particolare legge gli id della lista di oggetti 
const params = useLocalSearchParams<{ id: string }>();
// cerco nella array proverbs se l'id del parametro in input è uguale all'id di params restiuisce true, altrimenti restituisce undefined
// lo salvo in una variabile per maggiore riusibilità
const proverb = proverbs.find(p => p.id === params.id);
```

**Analisi del codice**
`useLocalSearchParams`: 
- ==legge i parametri presenti nell'URL della schermata corrente e li restituisce come oggetto.== 
- Il `<{ id: string }>` tra i [[Lezione 4 - Array, Custom Types e Generic#Generic Types|generics]] ==dice a TypeScript che ti aspetti un parametro chiamato `id` di tipo `string`.==

Quando navighi verso `/proverbs/1`, Expo Router trasforma quel `1` in un parametro e lo rende disponibile come `params.id`. Quindi dopo questa riga `params` è un oggetto del tipo:
```tsx
{ id: "1" } // se hai navigato verso /proverbs/1
{ id: "2" } // se hai navigato verso /proverbs/2
```

- `const proverb = proverbs.find(p => p.id === params.id);`:
	- `find()` è un metodo nativo degli array JavaScript: 
		-  ==**scorre ogni elemento** e restituisce il primo per cui la condizione è `true`.== 
		- ==Se non trova nulla restituisce `undefined`.==

- La funzione freccia `p => p.id === params.id` è il **predicato**: 
	- ==ovvero la condizione da verificare per ogni elemento.== 
	- `p` è il nome arbitrario che dai ad ogni elemento dell'array durante l'iterazione — potevi chiamarlo `item`, `el`, o qualsiasi altra cosa.

==Quindi per ogni oggetto nell'array controlla se il suo `id` corrisponde all'`id` letto dall'URL. Quando trova la corrispondenza si ferma e restituisce quell'oggetto, che viene salvato in `proverb`.==

È importante gestire anche il caso in cui l'ID non corrisponda a nessun elemento, restituendo un messaggio di errore:
```tsx
// se la ricerca restituisce undefined quindi proverb è falsy
if (!proverb) {
    return (
    // restiuisco un messaggio di errore
        <View style={styles.container}>
            <Text style={styles.txtError}>Error: Not Found</Text>
        </View>
    );
}
```

**Analisi del codice:**

> [!remember] Ricorda che `proverbs.find()` restituisce `undefined` se non trova nessun elemento che soddisfa la condizione. 
> 
> Quindi `proverb` può essere o un oggetto `Proverb` oppure `undefined`.

`!proverb` sfrutta la **negazione logica** combinata con la **falsiness** di JavaScript: 
- ==`undefined` è un valore falsy, quindi `!undefined` è `true`.== 
- ==In altre parole, `if (!proverb)` si legge come "se proverb non esiste".==

Questo blocco è un pattern chiamato **early return**:
- ==se la condizione è vera, la funzione restituisce subito il JSX dell'errore e si ferma lì — il codice sotto non viene mai eseguito.== 

> [!hint] Questo evita di dover annidare tutto il resto in un `else`.
> 

In assenza di questo controllo, TypeScript stesso ti avvertirebbe: 
 sa che `proverb` potrebbe essere `undefined`, quindi non ti permetterebbe di accedere a `proverb.proverb` o `proverb.source` senza prima verificare che esista. 
==Il blocco `if (!proverb)` serve quindi sia come **guardia logica** che come **soddisfazione del type checker**.==
##### Navigare verso un percorso dinamico

Da `index.tsx` ci sono due modi equivalenti per raggiungere una schermata con percorso dinamico:

1. Il primo è il più diretto: 
	- ==si passa l'ID direttamente nella stringa del percorso==.
```tsx
<Link href='/proverbs/1' push asChild>
    <Button title="Push to /proverb/1" />
</Link>
```
l'ID è scritto **hardcoded nella stringa** del percorso. 
==Expo Router legge il segmento `1` e lo mappa automaticamente al parametro `[id]` definito nel nome del file.== 

> [!fail] **Funziona perfettamente ma è poco flessibile**
>  ==se vuoi navigare verso un ID diverso devi scrivere un altro `<Link>` con una stringa diversa.==

2. Il secondo è più esplicito: 
	- separa il pathname dai parametri, usando la notazione con le parentesi quadre:
```tsx
<Link href={{ pathname: '/proverbs/[id]', params: { id: '2' } }} push asChild>
    <Button title="push to /proverb/2" />
</Link>
```

Qui invece `href` riceve un oggetto con due campi separati: 
- `pathname` ==contiene la struttura del percorso con il segmento dinamico esplicito tra parentesi quadre,==
- `params` ==contiene i valori da iniettare in quei segmenti.==

Il vantaggio reale di questa forma si vede quando l'ID non è un valore fisso ma una variabile, ad esempio quando stai renderizzando una lista:
```tsx
proverbs.map(p => (
    <Link href={{ pathname: '/proverbs/[id]', params: { id: p.id } }} push asChild>
        <Button title={p.proverb} />
    </Link>
))
```
Entrambi producono lo stesso risultato. 

> [!hint] La seconda forma è preferibile quando l'ID è una variabile e non un valore hardcoded, perché rende più chiara la separazione tra struttura del percorso e dati.
> 

###### Codice completo
`src/app/proverbs/[id].tsx`
```tsx
import { StyleSheet, Text, View } from 'react-native';
import React from 'react';
import { useLocalSearchParams } from 'expo-router';

// definisco la forma degli oggetti proverb
type Proverb = {
    id: string;
    proverb: string;
    source: string;
};

// array di dati statici tipizzato come Proverb[]
const proverbs: Proverb[] = [
    { id: "1", proverb: "Il momento migliore per piantare un albero era 20 anni fa. Il secondo momento migliore è adesso.", source: "Proverbio Cinese" },
    { id: "2", proverb: "Non importa quanto vai piano, l'importante è non fermarsi.", source: "Confucio" },
    // ...
];

const ProverbsScreen = () => {
    // leggo il segmento dinamico dall'URL
    const params = useLocalSearchParams<{ id: string }>();
    // cerco il proverbio corrispondente all'id ricevuto
    const proverb = proverbs.find(p => p.id === params.id);

    // early return: se l'id non corrisponde a nessun elemento mostro l'errore
    if (!proverb) {
        return (
            <View style={styles.container}>
                <Text style={styles.txtError}>Error: {params.id} Not Found</Text>
            </View>
        );
    }

    return (
        <View style={styles.container}>
            <Text style={styles.header}>"{proverb.proverb}"</Text>
            <Text>- {proverb.source}</Text>
        </View>
    );
};

export default ProverbsScreen;
```

`index.tsx` — i due link verso il percorso dinamico

```tsx
{/* forma diretta: ID hardcoded nella stringa */}
<Link href='/proverbs/1' push asChild>
    <Button title="Push to /proverb/1" />
</Link>

{/* forma esplicita: pathname e params separati */}
<Link href={{ pathname: '/proverbs/[id]', params: { id: '2' } }} push asChild>
    <Button title="push to /proverb/2" />
</Link>
```

> [!abstract] **Il flusso completo è:**
>  ==`index.tsx` naviga verso `/proverbs/1` → Expo Router mappa il segmento `1` al file `[id].tsx` → `useLocalSearchParams` lo legge come `params.id` → `proverbs.find()` cerca l'elemento corrispondente → il componente renderizza il proverbio o il messaggio di errore.==

### Rotte dinamiche annidate 
È possibile avere **più segmenti dinamici** all'interno dello stesso percorso. Per una schermata che mostra un prodotto filtrato per categoria, la struttura delle cartelle sarà:
```css
app/
└── products/
    └── [category]/
        └── [product].tsx
```

Sia la categoria che l'ID del prodotto sono dinamici, quindi navigando verso `/products/shoes/1234` Expo Router mapperà automaticamente `shoes` a `category` e `1234` a `product`.

##### Leggere più segmenti dinamici

`useLocalSearchParams` funziona esattamente come nel caso singolo — restituisce un oggetto con tutti i segmenti dinamici come chiavi:



```tsx
const ProductScreen = () => {
    const params = useLocalSearchParams();

    return (
        <View style={styles.container}>
            {/* JSON.stringify converte l'oggetto params in stringa leggibile */}
            <Text>{JSON.stringify(params, null, '')}</Text>
        </View>
    );
};
```

`JSON.stringify(params, null, '')`: 
- ==è usato qui solo a scopo dimostrativo per visualizzare il contenuto grezzo di `params`.== 
- ==Il risultato sarà qualcosa come `{"category":"shoes","product":"1234"}`.==

In un caso reale tipizzeresti e destruttureresti i parametri:
```tsx
const { category, product } = useLocalSearchParams<{ category: string; product: string }>();
```
quando tornerò alla pagina `index.tsx` e aggiungerò un link del tipo "`product/shoes/1234`", potremo vedere qui entrambi i segmenti dinamici del percorso

##### Navigare verso una rotta annidata dinamica

Da `index.tsx` si naviga esattamente come per una rotta dinamica semplice:

```tsx
<Link href='/products/shoes/1234' push asChild>

          <Button title="push to /products" />

        </Link>
```
==Expo Router si occupa di scomporre il percorso e distribuire i segmenti ai parametri corrispondenti in base alla struttura delle cartelle.==

### Opzioni Schermata  
Fino ad ora lo Stack in `_layout.tsx` gestiva tutte le schermate automaticamente senza che fossero dichiarate esplicitamente. 
È però possibile **elencare le schermate dentro lo Stack** tramite `<Stack.Screen>` per configurarle individualmente, passando il percorso tramite `name` e le opzioni tramite `options`.

Il prop `name` deve corrispondere esattamente al percorso del file senza la barra iniziale — quindi `proverbs/[id]` e non `/proverbs/`

##### Titolo statico

Il caso più semplice è passare un oggetto fisso a `options`:
```tsx
<Stack.Screen
    name='proverbs/[id]'
    options={{ title: 'Proverb' }}
/>
```
Questo sovrascrive il titolo di default, che altrimenti sarebbe il percorso grezzo — non molto leggibile.

##### Titolo dinamico dal layout

Per le schermate con percorsi dinamici il titolo statico rimane sempre lo stesso. Si può trasformare `options` in una funzione che riceve il `route` e restituisce l'oggetto delle opzioni costruito dinamicamente:

```tsx
<Stack.Screen
    name='proverbs/[id]'
    options={({ route }) => ({
        title: 'Proverb ID: ' + route.params?.id
    })}
/>
```

Mostrare l'ID però non è molto elegante. Il problema è che dal layout non si ha accesso ai dati della schermata — solo ai parametri del percorso.



##### Titolo dinamico dalla schermata

Quando il titolo dipende da dati disponibili solo dentro la schermata, Expo Router permette di configurare le opzioni **dall'interno del componente stesso** usando `<Stack.Screen>` senza il prop `name`:

```tsx
return (
    <View style={styles.container}>
        <Stack.Screen options={{ title: proverb.source }} />
        <Text style={styles.header}>"{proverb.proverb}"</Text>
        <Text>- {proverb.source}</Text>
    </View>
);
```

In questo caso il titolo mostrerà la fonte del proverbio, che è un'informazione accessibile solo dentro `[id].tsx`.

##### Precedenza delle opzioni

Le opzioni definite in `_layout.tsx` e quelle definite dentro la schermata non si annullano a vicenda — si **fondono**. La regola è semplice: 
- ==**più sei vicino alla schermata, più hai precedenza**.==

`_layout.tsx` è: 
- ==il posto dove si definiscono le opzioni di default per tutte le schermate dello stack — è necessariamente generico, perché non ha accesso ai dati delle singole schermate.==

`[id].tsx`: invece è la schermata stessa: 
- ha accesso a tutto — parametri, dati, stato locale. 
- ==Quando si definisce `<Stack.Screen options={...} />` al suo interno, Expo Router capisce che quelle opzioni sono più specifiche e le applica sopra quelle del layout.==

Immagina di avere nel layout:
```TSX
// _layout.tsx
<Stack.Screen
    name='proverbs/[id]'
    options={{ title: 'Proverb', headerShown: true }}
/>
```

E dentro la schermata:
```TSX
// proverbs/[id].tsx
<Stack.Screen options={{ title: proverb.source }} />
```

Il risultato finale sarà:
```TSX
{ title: proverb.source, headerShown: true }
```


Applicando la regola per ogni proprietà:

- `title` è definito in entrambi → ==vince quello della schermata: `proverb.source`==
- `headerShown` è definito solo nel layout → ==viene applicato così com'è==

> [!HELP] **Il caso pratico del tutorial segue esattamente questa logica:**
> 
> - nel layout si imposta `title: 'Proverb'` come fallback generico, e dentro `[id].tsx` lo si sovrascrive con `title: proverb.source` non appena i dati del proverbio sono disponibili.

> [!hint] Per esplorare tutte le opzioni disponibili — titolo, stile dell'intestazione, pulsanti, animazioni, ecc. — si può usare `CTRL + Spazio` nell'editor per attivare l'autocomplete sui tipi TypeScript di `options`.

##### Il prop `name`
```tsx
<Stack.Screen name='proverbs/[id]' />
```
`name` è :
- ==il **riferimento al file** dentro la cartella `app/`.==
- ==Expo Router usa il filesystem come sistema di routing, quindi il valore di `name` deve corrispondere esattamente al percorso del file relativo alla cartella `app/`, senza la barra iniziale e senza l'estensione `.tsx`.==

Alcuni esempi:

| File                                    | `name` corretto                 |
| --------------------------------------- | ------------------------------- |
| `app/index.tsx`                         | `index`                         |
| `app/second.tsx`                        | `second`                        |
| `app/proverbs/[id].tsx`                 | `proverbs/[id]`                 |
| `app/products/[category]/[product].tsx` | `products/[category]/[product]` |

> [!caution] **Se il valore di `name` non corrisponde a nessun file, la configurazione viene semplicemente ignorata.**
> 

##### Il prop `options`

`options` è il [[Lezione 2 - Il Props Object#Il Props Object|prop]] che: 
- ==permette di configurare l'aspetto e il comportamento della schermata.==
Accetta due forme:

1. **Oggetto statico** — quando le opzioni non dipendono da dati dinamici:
```tsx
<Stack.Screen
    name='index'
    options={{ title: 'Home' }}
/>
```

2. **Funzione** — quando le opzioni dipendono dai parametri del percorso:
```tsx
<Stack.Screen
    name='proverbs/[id]'
    options={({ route }) => ({
        title: 'Proverb ID: ' + route.params?.id
    })}
/>
```

La funzione riceve un oggetto con `route` destrutturato e restituisce l'oggetto delle opzioni. `route.params` contiene i parametri del percorso — nel caso di `proverbs/[id]`, conterrà `{ id: '1' }` o qualsiasi ID sia stato passato.

###### I parametri di `options`

Le proprietà più comuni che puoi passare dentro `options`:

| Proprietà          | Tipo         | Descrizione                              |
| ------------------ | ------------ | ---------------------------------------- |
| `title`            | `string`     | testo mostrato nell'header               |
| `headerShown`      | `boolean`    | mostra o nasconde l'header               |
| `headerStyle`      | `object`     | stile del contenitore dell'header        |
| `headerTintColor`  | `string`     | colore del titolo e della freccia Back   |
| `headerTitleStyle` | ``object``   | stile del testo del titolo               |
| `headerRight`      | ``function`` | componente custom a destra dell'header   |
| `headerLeft`       | ``function`` | componente custom a sinistra dell'header |
| `animation`        | `string`     | tipo di animazione di transizione        |
Ad esempio per personalizzare l'header della schermata dei proverbi:
```tsx
<Stack.Screen
    name='proverbs/[id]'
    options={{
        title: 'Proverbi',
        headerStyle: { backgroundColor: '#d21818' },
        headerTintColor: '#fff',
        headerTitleStyle: { fontWeight: 'bold' }
    }}
/>
```


> [!hint] **Per l'elenco completo usa `CTRL + Spazio` dentro `options={{}}` nel tuo editor — TypeScript mostrerà tutte le proprietà disponibili con i relativi tipi.**


### Configurare le animazioni della schermata

Tra le opzioni configurabili c'è anche il modo in cui la schermata entra in scena. Il comportamento di default varia per piattaforma:

- su **iOS** la schermata scivola da destra
- su **Android** c'è un effetto di dissolvenza con scorrimento verso l'alto

Tramite la proprietà `animation` dentro `options` è possibile sovrascrivere questo comportamento per tutte le piattaforme contemporaneamente:
```tsx
<Stack.Screen
    name='proverbs/[id]'
    options={({ route }) => ({
        title: 'Proverb ID: ' + route.params?.id,
        animation: 'slide_from_bottom'
    })}
/>
```


I valori più comuni per `animation` sono:

| Valore              | Comportamento                        |
| ------------------- | ------------------------------------ |
| `default`           | comportamento nativo per piattaforma |
| `slide_from_right`  | scivola da destra (default iOS)      |
| `slide_from_bottom` | scivola dal basso                    |
| `slide_from_left`   | scivola da sinistra                  |
| `fade`              | dissolvenza                          |
| `none`              | nessuna animazione                   |
>[!hint] Usare `none` può essere utile durante lo sviluppo per velocizzare la navigazione mentre si testa, oppure in produzione per schermate che devono apparire istantaneamente come splash screen o loading screen.

