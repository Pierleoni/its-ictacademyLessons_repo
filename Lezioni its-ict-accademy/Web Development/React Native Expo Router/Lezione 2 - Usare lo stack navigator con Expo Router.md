


# Introduzione: Usare lo Stack Navigator con Expo Router

Lo Stack è:
- ==uno dei principali strumenti di navigazione che permette di spostarci tra le schermate sui dispositivi mobili.== 
In questa lezione impareremo come navigare e trasferire dati tra le schermate all'interno di uno stack.

Nelle sezioni precedenti abbiamo costruito le fondamenta: 
sappiamo come [[Lezione 1 - Introduzione a EXPO SDK 55 e Navigazione#Percorsi e cartelle|strutturare le route con file e cartelle]], come [[Lezione 1 - Introduzione a EXPO SDK 55 e Navigazione#Schermate e file di Layout|i layout si annidano]] e [[Lezione 1 - Introduzione a EXPO SDK 55 e Navigazione#Ordine di esecuzione dei file di `_layout`|si eseguono dall'esterno verso l'interno]], come [[Lezione 1 - Introduzione a EXPO SDK 55 e Navigazione#Linking tra le schermate|`<Link>`]] e [[Lezione 1 - Introduzione a EXPO SDK 55 e Navigazione#`useRouter()`|`useRouter()`]] permettono di navigare tra le schermate, e come lo [[Lezione 1 - Introduzione a EXPO SDK 55 e Navigazione#^752b8b|`<Stack />`]] mantiene [[Lezione 1 - Introduzione a EXPO SDK 55 e Navigazione#Lo stack di navigazione|la pila delle schermate visitate]].

Tuttavia fino ad ora abbiamo usato lo `<Stack />` in modo minimale — lo abbiamo dichiarato nel root layout e lasciato fare il suo lavoro in modo automatico. Nella pratica, lo Stack navigator è molto più potente e configurabile di così.

In questa lezione lo esploriamo in profondità. Partiremo dalla navigazione di base per poi affrontare scenari più complessi:

- **Navigazione in uno stack** — come funziona la pila nel dettaglio e come controllarla
- **Ritorno a una schermata già esistente** — cosa succede quando la schermata di destinazione è già presente nello stack
- **Sostituzione della schermata corrente** — quando e come usare `replace` in modo consapevole
- **Opzioni di navigazione** — come configurare le transizioni e il comportamento dello stack
- **Passaggio di parametri tra le schermate** — come mandare dati da una schermata all'altra durante la navigazione
- **Percorsi dinamici** — come creare route parametriche che si adattano ai dati, come `/products/[id]`
- **Percorsi dinamici annidati** — come gestire route dinamiche a più livelli di profondità
- **Opzioni di schermata** — come personalizzare header, titolo e stile di ogni singola schermata

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
Sequenza di navigazione: I`ndex → Second → Third → **replace** → Index → Second → Third.`

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

 È un [[Lezione 3 - Hooks#Cosa sono gli Hooks|hook]] che permette di **leggere i parametri passati durante la navigazione** nella schermata corrente. 
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
È possibile rendere dinamico un segmento di un percorso racchiudendolo tra parentesi quadre. 
Voglio creare una schermata che mostri alcuni proverbi, quindi voglio che il titolo sia "proverbi" e il proverbio sia indicato dall'ID; 
creerò quindi una cartella chiamata "proverbi" e un file con l'ID tra parentesi quadre, in modo che questa parte sia dinamica. Non aggiungerò un file di layout qui perché voglio che questa schermata sia ancora gestita dallo Stack nel file `_layout.tsx` nella radice del progetto.
Quindi faremo un'esportazione predefinita per la schermata "`ProverbsScreen.tsx`" e otterremo una visualizzazione a pagina intera con spazio per il proverbio e la fonte.
```tsx
const ProverbsScreen = () => {

  return (

    <View style={styles.container}>

      <Text style = {styles.header}>ProverbsScreen</Text>

      <Text>-Source</Text>

    </View>

  );

};

  

export default ProverbsScreen;

  

const styles = StyleSheet.create({

  container: {

    flex: 1,

    justifyContent: 'center',

    alignItems: 'center',

    padding: 16,

    // gap: 8

  },

  header: {

    fontSize: 24,

    color: '#d21818ff'

  }

});
```

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

Ora dobbiamo accedere a questo ID per sapere quale proverbio mostrare, e lo facciamo utilizzando `useLocalSearchParams`, che possiamo anche tipizzare: 
```tsx
const ProverbsScreen = () => {

    const params = useLocalSearchParams<{id:string}>();

    return (

        <View style={styles.container}>

            <Text style={styles.header}>ProverbsScreen</Text>

            <Text>-Source</Text>

        </View>

    );

};
```

Quindi cerchiamo il proverbio dalla nostra lista

```tsx
const ProverbsScreen = () => {

    const params = useLocalSearchParams<{id:string}>();

    const proverb = proverbs.find(p=>p.id === params.id)

    return (

        <View style={styles.container}>

            <Text style={styles.header}>ProverbsScreen</Text>

            <Text>-Source</Text>

        </View>

    );

};
```

e dovremo anche gestire il caso in cui non venga trovato, quindi nel caso in cui non ci sia il proverbio con l'ID specificato, altrimenti lo visualizzeremo: 
```tsx
const ProverbsScreen = () => {

    const params = useLocalSearchParams<{ id: string }>();

    const proverb = proverbs.find(p => p.id === params.id)

    if (!proverb) {

        return (

            <View style={styles.container}>

                <Text style={styles.txtError}  >Error: {params.id} Not Found</Text>

            </View>

        )

    }

    return (

        <View style={styles.container}>

            <Text style={styles.header}>{proverb.proverb}</Text>

            <Text>- {proverb.source}</Text>

        </View>

    );

};
```

%% Continuare il video da min 7:29 %%