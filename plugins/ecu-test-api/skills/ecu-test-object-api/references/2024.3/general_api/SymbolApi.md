# API for Symbols[¶](#api-for-symbols "Link to this heading")

Part of the [Object based program API](objectApi.md#objectapi)

## SymbolApi[¶](#symbolapi "Link to this heading")

*class* SymbolApi[¶](#ApiClient.SymbolApi "Link to this definition")  
Returned by

- [`SignalApi.SymbolApi`](SignalApi.md#ApiClient.SignalApi.SymbolApi "ApiClient.SignalApi.SymbolApi")

CreateConstSymbol(*expression*)[¶](#ApiClient.SymbolApi.CreateConstSymbol "Link to this definition")  
Creates constant symbol

Parameters:  **expression** (*str*) – the expression

Returns:  New ConstSymbol

Return type:  [`ConstSymbol`](#ApiClient.ConstSymbol "ApiClient.ConstSymbol")

CreateSignalSymbol(*signalName*)[¶](#ApiClient.SymbolApi.CreateSignalSymbol "Link to this definition")  
Creates string symbol

Parameters:  **signalName** (*str*) – The signal description name

Returns:  New SignalSymbol

Return type:  [`SignalSymbol`](#ApiClient.SignalSymbol "ApiClient.SignalSymbol")

CreateStringSymbol(*value*)[¶](#ApiClient.SymbolApi.CreateStringSymbol "Link to this definition")  
Creates string symbol

Parameters:  **value** (*str*) – the string symbol name

Returns:  New StringSymbol

Return type:  [`StringSymbol`](#ApiClient.StringSymbol "ApiClient.StringSymbol")

## ConstSymbol[¶](#constsymbol "Link to this heading")

*class* ConstSymbol[¶](#ApiClient.ConstSymbol "Link to this definition")  
Base class

[`SymbolType`](SignalApi.md#ApiClient.SymbolType "ApiClient.SymbolType")

Returned by

- [`SymbolApi.CreateConstSymbol`](#ApiClient.SymbolApi.CreateConstSymbol "ApiClient.SymbolApi.CreateConstSymbol")

Clone()[¶](#ApiClient.ConstSymbol.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`ConstSymbol`](#ApiClient.ConstSymbol "ApiClient.ConstSymbol")

GetExpression()[¶](#ApiClient.ConstSymbol.GetExpression "Link to this definition")  
Returns the expression of the constant symbol

Returns:  Expression of constant symbol

Return type:  str

## SignalSymbol[¶](#signalsymbol "Link to this heading")

*class* SignalSymbol[¶](#ApiClient.SignalSymbol "Link to this definition")  
Base class

[`SymbolType`](SignalApi.md#ApiClient.SymbolType "ApiClient.SymbolType")

Returned by

- [`SymbolApi.CreateSignalSymbol`](#ApiClient.SymbolApi.CreateSignalSymbol "ApiClient.SymbolApi.CreateSignalSymbol")

Clone()[¶](#ApiClient.SignalSymbol.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`SignalSymbol`](#ApiClient.SignalSymbol "ApiClient.SignalSymbol")

GetSignalName()[¶](#ApiClient.SignalSymbol.GetSignalName "Link to this definition")  
Returns the signal description name of the signal symbol

Returns:  The signal description name

Return type:  str

## StringSymbol[¶](#stringsymbol "Link to this heading")

*class* StringSymbol[¶](#ApiClient.StringSymbol "Link to this definition")  
Base class

[`SymbolType`](SignalApi.md#ApiClient.SymbolType "ApiClient.SymbolType")

Returned by

- [`SymbolApi.CreateStringSymbol`](#ApiClient.SymbolApi.CreateStringSymbol "ApiClient.SymbolApi.CreateStringSymbol")

Clone()[¶](#ApiClient.StringSymbol.Clone "Link to this definition")  
Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.

Returns:  A copy of this object

Return type:  [`StringSymbol`](#ApiClient.StringSymbol "ApiClient.StringSymbol")

GetValue()[¶](#ApiClient.StringSymbol.GetValue "Link to this definition")  
Returns the value of the string symbol

Returns:  Value of string symbol

Return type:  str
