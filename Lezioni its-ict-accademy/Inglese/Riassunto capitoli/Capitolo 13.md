# Automazione domestica e pensiero computazionale

#### Struttura del Sistema di Automazione

Il sistema di automazione domestica è diviso in due pacchetti principali:

1. **Core**: Contiene le parti centrali del sistema, che includono classi generiche come `Rule`, `Component` e `Sensor`.
    
2. **Subsystems**: Include i sottosistemi specifici come il riscaldamento, la ventilazione e l'illuminazione, che implementano regole e componenti specifici per ciascun ambito.
    

#### Componenti e Regole

- **Rule**: Classe base per applicare regole a letture e componenti, destinata a essere estesa.
    
- **Component**: Rappresenta un componente come un riscaldatore o una luce, che può essere acceso o spento.
    
- **Sensor**: Classe base per sensori che prendono letture da un ambiente, da implementare in modo specifico per ciascun tipo di sensore.
    

#### Esempio di sottosistema di riscaldamento

Il sottosistema di riscaldamento utilizza:

- **Radiator**: Un componente che può essere acceso o spento.
    
- **TemperatureRule**: Una regola che accende o spegne il riscaldatore in base alla temperatura (ad esempio, accende il riscaldatore sotto i 18°C e lo spegne sopra i 22°C).
    
- **TemperatureSensor**: Un sensore che prende letture casuali della temperatura tra 16°C e 25°C.
    

#### Esempio di sottosistema di ventilazione

Il sottosistema di ventilazione utilizza:

- **Ventilator**: Un componente che può essere acceso o spento.
    
- **VentilationRule**: Una regola che accende la ventilazione se l'umidità è superiore al 70% o tra le 17:00 e le 20:00.
    
- **MoistureSensor**: Un sensore che misura l'umidità, con valori casuali tra 30% e 80%.
    

#### Esempio di sottosistema di illuminazione

Il sottosistema di illuminazione utilizza:

- **Light**: Un componente che può essere acceso o spento.
    
- **LightingRule**: Una regola che accende la luce quando la stanza è occupata e la spegne dopo un countdown di 5 minuti (300 secondi).
    
- **LightSensor**: Un sensore che rileva se la stanza è occupata o meno con un valore casuale.
    

#### Regolatore

Il **Regulator** è una classe che gestisce le letture dei sensori e applica le regole corrispondenti ai componenti. Gestisce più stanze e può applicare una regola per ogni stanza.

#### Test

I test sono organizzati in due livelli:

1. **Unit Test**: Testano il comportamento di singoli componenti o regole (ad esempio, test di `LightingRule`).
    
2. **System Test**: Testano l'integrazione di più componenti e regole, simulando il comportamento dell'intero sistema (ad esempio, test di un sottosistema di riscaldamento).
    

I test usano il framework `unittest` di Python e verificano che le regole e i componenti interagiscano correttamente, come nel caso del riscaldamento che si accende quando la temperatura è bassa.

#### Miglioramenti Possibili

Alcuni miglioramenti suggeriti per il sistema includono:

- Aggiungere un pannello di controllo.
    
- Supportare più regole in un regolatore (ad esempio, per la ventilazione con umidità e tempo separati).
    
- Aggiungere componenti con stato più sofisticato (ad esempio, luci dimmerabili).
    
- Aggiungere log per il monitoraggio e il debugging.
    
- Scrivere un test di sistema che simuli il funzionamento di tutti i sottosistemi contemporaneamente.
    
- Migliorare il countdown dell'illuminazione per renderlo indipendente dal regolatore o renderlo un thread separato.
    

Il capitolo esplora un esempio semplificato di automazione domestica, evidenziando come la progettazione del sistema possa essere evoluta per diventare una soluzione più sofisticata.


---
# Traduzione in inglese
## #### System Structure

The home automation system is divided into two main packages:

1. **Core**: Contains the central parts of the system, including generic classes such as `Rule`, `Component`, and `Sensor`.
    
2. **Subsystems**: Includes specific subsystems like heating, ventilation, and lighting, which implement specific rules and components for each domain.
    

#### Components and Rules

- **Rule**: A base class for applying rules to readings and components, intended to be extended.
    
- **Component**: Represents a component like a heater or a light that can be turned on or off.
    
- **Sensor**: A base class for sensors that take readings from an environment, to be implemented specifically for each sensor type.
    

#### Heating Subsystem Example

The heating subsystem uses:

- **Radiator**: A component that can be turned on or off.
    
- **TemperatureRule**: A rule that turns the radiator on if the temperature is below 18°C and turns it off if it is above 22°C.
    
- **TemperatureSensor**: A sensor that takes random temperature readings between 16°C and 25°C.
    

#### Ventilation Subsystem Example

The ventilation subsystem uses:

- **Ventilator**: A component that can be turned on or off.
    
- **VentilationRule**: A rule that turns on the ventilator if the humidity is above 70% or between 5:00 PM and 8:00 PM.
    
- **MoistureSensor**: A sensor that measures humidity with random values between 30% and 80%.
    

#### Lighting Subsystem Example

The lighting subsystem uses:

- **Light**: A component that can be turned on or off.
    
- **LightingRule**: A rule that turns on the light when the room is occupied and turns it off after a 5-minute countdown (300 seconds).
    
- **LightSensor**: A sensor that detects whether the room is occupied or not with a random value.
    

#### Regulator

The **Regulator** is a class that manages sensor readings and applies the corresponding rules to the components. It manages multiple rooms and can apply a rule for each room.

#### Tests

Tests are organized into two levels:

1. **Unit Test**: Tests the behavior of individual components or rules (e.g., testing `LightingRule`).
    
2. **System Test**: Tests the integration of multiple components and rules, simulating the behavior of the entire system (e.g., testing a heating subsystem).
    

Tests use the `unittest` framework in Python and check that the rules and components interact correctly, such as the heater turning on when the temperature is low.

#### Possible Improvements

Some suggested improvements for the system include:

- Adding a control panel.
    
- Supporting multiple rules in one regulator (e.g., for ventilation with separate humidity and time rules).
    
- Adding components with more sophisticated states (e.g., dimmable lights).
    
- Adding logging for monitoring and debugging.
    
- Writing a system test that simulates the operation of all subsystems at the same time.
    
- Improving the lighting countdown to make it independent of the regulator or to make it a separate thread.
    

This chapter explores a simplified example of home automation, highlighting how the system design can evolve into a more sophisticated solution.