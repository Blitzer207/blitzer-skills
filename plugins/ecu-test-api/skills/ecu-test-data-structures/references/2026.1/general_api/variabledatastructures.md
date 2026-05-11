[ Internal APIs ](api.md)

Advanced operations of package variable types [ Advanced operations of package variable types ](#)

Advanced operations of package variable types

- [ ByteStream ](#bytestream)
  - [C ByteStream ](#tts.lib.dataStructures.ByteStream.ByteStream)
    - [M Count ](#tts.lib.dataStructures.ByteStream.ByteStream.Count)
    - [M Find ](#tts.lib.dataStructures.ByteStream.ByteStream.Find)
    - [M FromIntelWordList ](#tts.lib.dataStructures.ByteStream.ByteStream.FromIntelWordList)
    - [M FromMotorolaWordList ](#tts.lib.dataStructures.ByteStream.ByteStream.FromMotorolaWordList)
    - [M FromRawString ](#tts.lib.dataStructures.ByteStream.ByteStream.FromRawString)
    - [M HexString ](#tts.lib.dataStructures.ByteStream.ByteStream.HexString)
    - [M IBits ](#tts.lib.dataStructures.ByteStream.ByteStream.IBits)
    - [M Index ](#tts.lib.dataStructures.ByteStream.ByteStream.Index)
    - [M IntelWordList ](#tts.lib.dataStructures.ByteStream.ByteStream.IntelWordList)
    - [M Ints ](#tts.lib.dataStructures.ByteStream.ByteStream.Ints)
    - [M Legacy ](#tts.lib.dataStructures.ByteStream.ByteStream.Legacy)
    - [M MBits ](#tts.lib.dataStructures.ByteStream.ByteStream.MBits)
    - [M Match ](#tts.lib.dataStructures.ByteStream.ByteStream.Match)
    - [M MotorolaWordList ](#tts.lib.dataStructures.ByteStream.ByteStream.MotorolaWordList)
    - [M RawString ](#tts.lib.dataStructures.ByteStream.ByteStream.RawString)
    - [M Reverse ](#tts.lib.dataStructures.ByteStream.ByteStream.Reverse)
    - [M SetIBits ](#tts.lib.dataStructures.ByteStream.ByteStream.SetIBits)
    - [M SetMBits ](#tts.lib.dataStructures.ByteStream.ByteStream.SetMBits)
    - [A bsClass ](#tts.lib.dataStructures.ByteStream.ByteStream.bsClass)
- [ BitStream ](#bitstream)
  - [C BitStream ](#tts.lib.dataStructures.BitStream.BitStream)
    - [M Bin ](#tts.lib.dataStructures.BitStream.BitStream.Bin)
    - [M Double ](#tts.lib.dataStructures.BitStream.BitStream.Double)
    - [M Float ](#tts.lib.dataStructures.BitStream.BitStream.Float)
    - [M FromBin ](#tts.lib.dataStructures.BitStream.BitStream.FromBin)
    - [M FromDouble ](#tts.lib.dataStructures.BitStream.BitStream.FromDouble)
    - [M FromFloat ](#tts.lib.dataStructures.BitStream.BitStream.FromFloat)
    - [M FromInt ](#tts.lib.dataStructures.BitStream.BitStream.FromInt)
    - [M FromRawString ](#tts.lib.dataStructures.BitStream.BitStream.FromRawString)
    - [M FromUInt ](#tts.lib.dataStructures.BitStream.BitStream.FromUInt)
    - [M IBytes ](#tts.lib.dataStructures.BitStream.BitStream.IBytes)
    - [M Int ](#tts.lib.dataStructures.BitStream.BitStream.Int)
    - [M MBytes ](#tts.lib.dataStructures.BitStream.BitStream.MBytes)
    - [M Pad ](#tts.lib.dataStructures.BitStream.BitStream.Pad)
    - [M Pad4 ](#tts.lib.dataStructures.BitStream.BitStream.Pad4)
    - [M Pad8 ](#tts.lib.dataStructures.BitStream.BitStream.Pad8)
    - [M UInt ](#tts.lib.dataStructures.BitStream.BitStream.UInt)
    - [A bsClass ](#tts.lib.dataStructures.BitStream.BitStream.bsClass)
- [ Vector ](#vector)
  - [C Vector ](#tts.core.package.dataStructures.Vector.Vector)
    - [M GetDimension ](#tts.core.package.dataStructures.Vector.Vector.GetDimension)
    - [M SetValue ](#tts.core.package.dataStructures.Vector.Vector.SetValue)
    - [M GetValue ](#tts.core.package.dataStructures.Vector.Vector.GetValue)
    - [M DeleteValue ](#tts.core.package.dataStructures.Vector.Vector.DeleteValue)
    - [M List ](#tts.core.package.dataStructures.Vector.Vector.List)
    - [M ToNumpyArray ](#tts.core.package.dataStructures.Vector.Vector.ToNumpyArray)
    - [M `\_\_add\_\_` ](#tts.core.package.dataStructures.Vector.Vector.__add__)
    - [M `\_\_sub\_\_` ](#tts.core.package.dataStructures.Vector.Vector.__sub__)
    - [M `\_\_mul\_\_` ](#tts.core.package.dataStructures.Vector.Vector.__mul__)
    - [M `\_\_truediv\_\_` ](#tts.core.package.dataStructures.Vector.Vector.__truediv__)
- [ Matrix ](#matrix)
  - [C Matrix ](#tts.core.package.dataStructures.Matrix.Matrix)
    - [M GetXDimension ](#tts.core.package.dataStructures.Matrix.Matrix.GetXDimension)
    - [M GetYDimension ](#tts.core.package.dataStructures.Matrix.Matrix.GetYDimension)
    - [M GetValue ](#tts.core.package.dataStructures.Matrix.Matrix.GetValue)
    - [M SetValue ](#tts.core.package.dataStructures.Matrix.Matrix.SetValue)
    - [M DeleteValue ](#tts.core.package.dataStructures.Matrix.Matrix.DeleteValue)
    - [M GetRow ](#tts.core.package.dataStructures.Matrix.Matrix.GetRow)
    - [M GetCol ](#tts.core.package.dataStructures.Matrix.Matrix.GetCol)
    - [M List ](#tts.core.package.dataStructures.Matrix.Matrix.List)
    - [M ToNumpyArray ](#tts.core.package.dataStructures.Matrix.Matrix.ToNumpyArray)
    - [M `\_\_add\_\_` ](#tts.core.package.dataStructures.Matrix.Matrix.__add__)
    - [M `\_\_sub\_\_` ](#tts.core.package.dataStructures.Matrix.Matrix.__sub__)
    - [M `\_\_mul\_\_` ](#tts.core.package.dataStructures.Matrix.Matrix.__mul__)
    - [M `\_\_truediv\_\_` ](#tts.core.package.dataStructures.Matrix.Matrix.__truediv__)
- [ Curve ](#curve)
  - [C Curve ](#tts.core.package.dataStructures.Curve.Curve)
    - [M SetDistributionValue ](#tts.core.package.dataStructures.Curve.Curve.SetDistributionValue)
    - [M GetDistributionValue ](#tts.core.package.dataStructures.Curve.Curve.GetDistributionValue)
    - [M DeleteDistributionValue ](#tts.core.package.dataStructures.Curve.Curve.DeleteDistributionValue)
    - [M GetDistribution ](#tts.core.package.dataStructures.Curve.Curve.GetDistribution)
    - [M List ](#tts.core.package.dataStructures.Curve.Curve.List)
    - [M Interpolate ](#tts.core.package.dataStructures.Curve.Curve.Interpolate)
    - [M GetDimension ](#tts.core.package.dataStructures.Curve.Curve.GetDimension)
    - [M GetValue ](#tts.core.package.dataStructures.Curve.Curve.GetValue)
    - [M SetValue ](#tts.core.package.dataStructures.Curve.Curve.SetValue)
    - [M ToNumpyArray ](#tts.core.package.dataStructures.Curve.Curve.ToNumpyArray)
- [ EnumDefinition ](#enumdefinition)
  - [C EnumDefinition ](#tts.core.package.dataStructures.Enum.EnumDefinition)
    - [M `\_\_iter\_\_` ](#tts.core.package.dataStructures.Enum.EnumDefinition.__iter__)
    - [M `\_\_getattr\_\_` ](#tts.core.package.dataStructures.Enum.EnumDefinition.__getattr__)
    - [M `\_\_getitem\_\_` ](#tts.core.package.dataStructures.Enum.EnumDefinition.__getitem__)
- [ EnumValue ](#enumvalue)
  - [C EnumValue ](#tts.core.package.dataStructures.Enum.EnumValue)
    - [M `\_\_eq\_\_` ](#tts.core.package.dataStructures.Enum.EnumValue.__eq__)
    - [A int ](#tts.core.package.dataStructures.Enum.EnumValue.int)
    - [A str ](#tts.core.package.dataStructures.Enum.EnumValue.str)
    - [A enum ](#tts.core.package.dataStructures.Enum.EnumValue.enum)
- [ Map ](#map)
  - [C Map ](#tts.core.package.dataStructures.Map.Map)
    - [M GetXDistribution ](#tts.core.package.dataStructures.Map.Map.GetXDistribution)
    - [M GetYDistribution ](#tts.core.package.dataStructures.Map.Map.GetYDistribution)
    - [M GetXDistributionValue ](#tts.core.package.dataStructures.Map.Map.GetXDistributionValue)
    - [M DeleteXDistributionValue ](#tts.core.package.dataStructures.Map.Map.DeleteXDistributionValue)
    - [M GetYDistributionValue ](#tts.core.package.dataStructures.Map.Map.GetYDistributionValue)
    - [M DeleteYDistributionValue ](#tts.core.package.dataStructures.Map.Map.DeleteYDistributionValue)
    - [M SetXDistributionValue ](#tts.core.package.dataStructures.Map.Map.SetXDistributionValue)
    - [M SetYDistributionValue ](#tts.core.package.dataStructures.Map.Map.SetYDistributionValue)
    - [M List ](#tts.core.package.dataStructures.Map.Map.List)
    - [M Interpolate ](#tts.core.package.dataStructures.Map.Map.Interpolate)
    - [M GetXDimension ](#tts.core.package.dataStructures.Map.Map.GetXDimension)
    - [M GetYDimension ](#tts.core.package.dataStructures.Map.Map.GetYDimension)
    - [M GetValue ](#tts.core.package.dataStructures.Map.Map.GetValue)
    - [M SetValue ](#tts.core.package.dataStructures.Map.Map.SetValue)
    - [M ToNumpyArray ](#tts.core.package.dataStructures.Map.Map.ToNumpyArray)
- [ StructuredSignal ](#structuredsignal)
  - [C StructuredSignal ](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignal)
    - [M GetName ](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignal.GetName)
    - [M GetElementNames ](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignal.GetElementNames)
    - [M IterElements ](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignal.IterElements)
- [ StructuredSignalLeaf ](#structuredsignalleaf)
  - [C StructuredSignalLeaf ](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf)
    - [M min ](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.min)
    - [M max ](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.max)
    - [M any ](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.any)
    - [M all ](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.all)
    - [M FullArray ](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.FullArray)
    - [M GetName ](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.GetName)
    - [M GetElementNames ](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.GetElementNames)
    - [M IterElements ](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.IterElements)
- [ Inbox ](#inbox)
  - [C Inbox ](#tts.core.package.dataStructures.Inbox.Inbox)
    - [M IsEmpty ](#tts.core.package.dataStructures.Inbox.Inbox.IsEmpty)
    - [M GetCount ](#tts.core.package.dataStructures.Inbox.Inbox.GetCount)
    - [M FetchNext ](#tts.core.package.dataStructures.Inbox.Inbox.FetchNext)
    - [M LookUpNext ](#tts.core.package.dataStructures.Inbox.Inbox.LookUpNext)
- [ Outbox ](#outbox)
  - [C Outbox ](#tts.core.package.dataStructures.Outbox.Outbox)
    - [M Post ](#tts.core.package.dataStructures.Outbox.Outbox.Post)
    - [M IsConnected ](#tts.core.package.dataStructures.Outbox.Outbox.IsConnected)

[ Advanced properties of bus-related objects ](busdatastructures.md)

[ Bus related objects of trace analysis ](busdatastructuresTraceanalysis.md)

[ Advanced properties of diagnostics-related objects ](diagdatastructures.md)

[ Diagnostics related objects of trace analysis ](diagdatastructuresTraceanalysis.md)

[ Advanced properties of media-related objects ](mediadatastructures.md)

[ Advanced properties of DLT logging-related objects ](dltdatastructures.md)

[ COM API ](com-api.md)

[ REST API ](rest-api.md)

[ Report API ](apireport.md)

[ Object API ](objectApi.md)

[ Trace Analysis API ](../TraceAnalysisAPI/index.md)

[ Generator APIs ](../generators/index.md)

[ Tools ](../tools/index.md)

[ User test management ](../userTestmanagement/index.md)

[ UserUtility API ](../user-utility/user-utility.md)

[ Utility Examples ](../user-utility/example-utilities.md)

Advanced operations of package variable types

- [ ByteStream ](#bytestream)
  - [C ByteStream ](#tts.lib.dataStructures.ByteStream.ByteStream)
    - [M Count ](#tts.lib.dataStructures.ByteStream.ByteStream.Count)
    - [M Find ](#tts.lib.dataStructures.ByteStream.ByteStream.Find)
    - [M FromIntelWordList ](#tts.lib.dataStructures.ByteStream.ByteStream.FromIntelWordList)
    - [M FromMotorolaWordList ](#tts.lib.dataStructures.ByteStream.ByteStream.FromMotorolaWordList)
    - [M FromRawString ](#tts.lib.dataStructures.ByteStream.ByteStream.FromRawString)
    - [M HexString ](#tts.lib.dataStructures.ByteStream.ByteStream.HexString)
    - [M IBits ](#tts.lib.dataStructures.ByteStream.ByteStream.IBits)
    - [M Index ](#tts.lib.dataStructures.ByteStream.ByteStream.Index)
    - [M IntelWordList ](#tts.lib.dataStructures.ByteStream.ByteStream.IntelWordList)
    - [M Ints ](#tts.lib.dataStructures.ByteStream.ByteStream.Ints)
    - [M Legacy ](#tts.lib.dataStructures.ByteStream.ByteStream.Legacy)
    - [M MBits ](#tts.lib.dataStructures.ByteStream.ByteStream.MBits)
    - [M Match ](#tts.lib.dataStructures.ByteStream.ByteStream.Match)
    - [M MotorolaWordList ](#tts.lib.dataStructures.ByteStream.ByteStream.MotorolaWordList)
    - [M RawString ](#tts.lib.dataStructures.ByteStream.ByteStream.RawString)
    - [M Reverse ](#tts.lib.dataStructures.ByteStream.ByteStream.Reverse)
    - [M SetIBits ](#tts.lib.dataStructures.ByteStream.ByteStream.SetIBits)
    - [M SetMBits ](#tts.lib.dataStructures.ByteStream.ByteStream.SetMBits)
    - [A bsClass ](#tts.lib.dataStructures.ByteStream.ByteStream.bsClass)
- [ BitStream ](#bitstream)
  - [C BitStream ](#tts.lib.dataStructures.BitStream.BitStream)
    - [M Bin ](#tts.lib.dataStructures.BitStream.BitStream.Bin)
    - [M Double ](#tts.lib.dataStructures.BitStream.BitStream.Double)
    - [M Float ](#tts.lib.dataStructures.BitStream.BitStream.Float)
    - [M FromBin ](#tts.lib.dataStructures.BitStream.BitStream.FromBin)
    - [M FromDouble ](#tts.lib.dataStructures.BitStream.BitStream.FromDouble)
    - [M FromFloat ](#tts.lib.dataStructures.BitStream.BitStream.FromFloat)
    - [M FromInt ](#tts.lib.dataStructures.BitStream.BitStream.FromInt)
    - [M FromRawString ](#tts.lib.dataStructures.BitStream.BitStream.FromRawString)
    - [M FromUInt ](#tts.lib.dataStructures.BitStream.BitStream.FromUInt)
    - [M IBytes ](#tts.lib.dataStructures.BitStream.BitStream.IBytes)
    - [M Int ](#tts.lib.dataStructures.BitStream.BitStream.Int)
    - [M MBytes ](#tts.lib.dataStructures.BitStream.BitStream.MBytes)
    - [M Pad ](#tts.lib.dataStructures.BitStream.BitStream.Pad)
    - [M Pad4 ](#tts.lib.dataStructures.BitStream.BitStream.Pad4)
    - [M Pad8 ](#tts.lib.dataStructures.BitStream.BitStream.Pad8)
    - [M UInt ](#tts.lib.dataStructures.BitStream.BitStream.UInt)
    - [A bsClass ](#tts.lib.dataStructures.BitStream.BitStream.bsClass)
- [ Vector ](#vector)
  - [C Vector ](#tts.core.package.dataStructures.Vector.Vector)
    - [M GetDimension ](#tts.core.package.dataStructures.Vector.Vector.GetDimension)
    - [M SetValue ](#tts.core.package.dataStructures.Vector.Vector.SetValue)
    - [M GetValue ](#tts.core.package.dataStructures.Vector.Vector.GetValue)
    - [M DeleteValue ](#tts.core.package.dataStructures.Vector.Vector.DeleteValue)
    - [M List ](#tts.core.package.dataStructures.Vector.Vector.List)
    - [M ToNumpyArray ](#tts.core.package.dataStructures.Vector.Vector.ToNumpyArray)
    - [M `\_\_add\_\_` ](#tts.core.package.dataStructures.Vector.Vector.__add__)
    - [M `\_\_sub\_\_` ](#tts.core.package.dataStructures.Vector.Vector.__sub__)
    - [M `\_\_mul\_\_` ](#tts.core.package.dataStructures.Vector.Vector.__mul__)
    - [M `\_\_truediv\_\_` ](#tts.core.package.dataStructures.Vector.Vector.__truediv__)
- [ Matrix ](#matrix)
  - [C Matrix ](#tts.core.package.dataStructures.Matrix.Matrix)
    - [M GetXDimension ](#tts.core.package.dataStructures.Matrix.Matrix.GetXDimension)
    - [M GetYDimension ](#tts.core.package.dataStructures.Matrix.Matrix.GetYDimension)
    - [M GetValue ](#tts.core.package.dataStructures.Matrix.Matrix.GetValue)
    - [M SetValue ](#tts.core.package.dataStructures.Matrix.Matrix.SetValue)
    - [M DeleteValue ](#tts.core.package.dataStructures.Matrix.Matrix.DeleteValue)
    - [M GetRow ](#tts.core.package.dataStructures.Matrix.Matrix.GetRow)
    - [M GetCol ](#tts.core.package.dataStructures.Matrix.Matrix.GetCol)
    - [M List ](#tts.core.package.dataStructures.Matrix.Matrix.List)
    - [M ToNumpyArray ](#tts.core.package.dataStructures.Matrix.Matrix.ToNumpyArray)
    - [M `\_\_add\_\_` ](#tts.core.package.dataStructures.Matrix.Matrix.__add__)
    - [M `\_\_sub\_\_` ](#tts.core.package.dataStructures.Matrix.Matrix.__sub__)
    - [M `\_\_mul\_\_` ](#tts.core.package.dataStructures.Matrix.Matrix.__mul__)
    - [M `\_\_truediv\_\_` ](#tts.core.package.dataStructures.Matrix.Matrix.__truediv__)
- [ Curve ](#curve)
  - [C Curve ](#tts.core.package.dataStructures.Curve.Curve)
    - [M SetDistributionValue ](#tts.core.package.dataStructures.Curve.Curve.SetDistributionValue)
    - [M GetDistributionValue ](#tts.core.package.dataStructures.Curve.Curve.GetDistributionValue)
    - [M DeleteDistributionValue ](#tts.core.package.dataStructures.Curve.Curve.DeleteDistributionValue)
    - [M GetDistribution ](#tts.core.package.dataStructures.Curve.Curve.GetDistribution)
    - [M List ](#tts.core.package.dataStructures.Curve.Curve.List)
    - [M Interpolate ](#tts.core.package.dataStructures.Curve.Curve.Interpolate)
    - [M GetDimension ](#tts.core.package.dataStructures.Curve.Curve.GetDimension)
    - [M GetValue ](#tts.core.package.dataStructures.Curve.Curve.GetValue)
    - [M SetValue ](#tts.core.package.dataStructures.Curve.Curve.SetValue)
    - [M ToNumpyArray ](#tts.core.package.dataStructures.Curve.Curve.ToNumpyArray)
- [ EnumDefinition ](#enumdefinition)
  - [C EnumDefinition ](#tts.core.package.dataStructures.Enum.EnumDefinition)
    - [M `\_\_iter\_\_` ](#tts.core.package.dataStructures.Enum.EnumDefinition.__iter__)
    - [M `\_\_getattr\_\_` ](#tts.core.package.dataStructures.Enum.EnumDefinition.__getattr__)
    - [M `\_\_getitem\_\_` ](#tts.core.package.dataStructures.Enum.EnumDefinition.__getitem__)
- [ EnumValue ](#enumvalue)
  - [C EnumValue ](#tts.core.package.dataStructures.Enum.EnumValue)
    - [M `\_\_eq\_\_` ](#tts.core.package.dataStructures.Enum.EnumValue.__eq__)
    - [A int ](#tts.core.package.dataStructures.Enum.EnumValue.int)
    - [A str ](#tts.core.package.dataStructures.Enum.EnumValue.str)
    - [A enum ](#tts.core.package.dataStructures.Enum.EnumValue.enum)
- [ Map ](#map)
  - [C Map ](#tts.core.package.dataStructures.Map.Map)
    - [M GetXDistribution ](#tts.core.package.dataStructures.Map.Map.GetXDistribution)
    - [M GetYDistribution ](#tts.core.package.dataStructures.Map.Map.GetYDistribution)
    - [M GetXDistributionValue ](#tts.core.package.dataStructures.Map.Map.GetXDistributionValue)
    - [M DeleteXDistributionValue ](#tts.core.package.dataStructures.Map.Map.DeleteXDistributionValue)
    - [M GetYDistributionValue ](#tts.core.package.dataStructures.Map.Map.GetYDistributionValue)
    - [M DeleteYDistributionValue ](#tts.core.package.dataStructures.Map.Map.DeleteYDistributionValue)
    - [M SetXDistributionValue ](#tts.core.package.dataStructures.Map.Map.SetXDistributionValue)
    - [M SetYDistributionValue ](#tts.core.package.dataStructures.Map.Map.SetYDistributionValue)
    - [M List ](#tts.core.package.dataStructures.Map.Map.List)
    - [M Interpolate ](#tts.core.package.dataStructures.Map.Map.Interpolate)
    - [M GetXDimension ](#tts.core.package.dataStructures.Map.Map.GetXDimension)
    - [M GetYDimension ](#tts.core.package.dataStructures.Map.Map.GetYDimension)
    - [M GetValue ](#tts.core.package.dataStructures.Map.Map.GetValue)
    - [M SetValue ](#tts.core.package.dataStructures.Map.Map.SetValue)
    - [M ToNumpyArray ](#tts.core.package.dataStructures.Map.Map.ToNumpyArray)
- [ StructuredSignal ](#structuredsignal)
  - [C StructuredSignal ](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignal)
    - [M GetName ](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignal.GetName)
    - [M GetElementNames ](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignal.GetElementNames)
    - [M IterElements ](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignal.IterElements)
- [ StructuredSignalLeaf ](#structuredsignalleaf)
  - [C StructuredSignalLeaf ](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf)
    - [M min ](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.min)
    - [M max ](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.max)
    - [M any ](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.any)
    - [M all ](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.all)
    - [M FullArray ](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.FullArray)
    - [M GetName ](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.GetName)
    - [M GetElementNames ](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.GetElementNames)
    - [M IterElements ](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.IterElements)
- [ Inbox ](#inbox)
  - [C Inbox ](#tts.core.package.dataStructures.Inbox.Inbox)
    - [M IsEmpty ](#tts.core.package.dataStructures.Inbox.Inbox.IsEmpty)
    - [M GetCount ](#tts.core.package.dataStructures.Inbox.Inbox.GetCount)
    - [M FetchNext ](#tts.core.package.dataStructures.Inbox.Inbox.FetchNext)
    - [M LookUpNext ](#tts.core.package.dataStructures.Inbox.Inbox.LookUpNext)
- [ Outbox ](#outbox)
  - [C Outbox ](#tts.core.package.dataStructures.Outbox.Outbox)
    - [M Post ](#tts.core.package.dataStructures.Outbox.Outbox.Post)
    - [M IsConnected ](#tts.core.package.dataStructures.Outbox.Outbox.IsConnected)

# Advanced operations of package variable types[¶](#advanced-operations-of-package-variable-types "Link to this heading")

The following types are globally available. E.g., in function variables, UserPyModules or other user code:

- [`BitStream`](#tts.lib.dataStructures.BitStream.BitStream "tts.lib.dataStructures.BitStream.BitStream (Python class) — The BitStream type is used to represent binary data. It is possible to represent leading zeros (in contrast to plain integers), as BitStream objects have a defined length. The BitStream type supports binary operations (in contrast to plain strings), sequence operations and checking for equality. When a binary operator has operands with different size, it pads the "shorter" BitStream with zeros until its size matches the size of the "larger" BitStream.")

- [`ByteStream`](#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

- [`Curve`](#tts.core.package.dataStructures.Curve.Curve "tts.core.package.dataStructures.Curve.Curve (Python class) — List of values")

- [`EnumDefinition`](#tts.core.package.dataStructures.Enum.EnumDefinition "tts.core.package.dataStructures.Enum.EnumDefinition (Python class) — Is returned when accessing the attribute enum of an EnumValue.")

- [`EnumValue`](#tts.core.package.dataStructures.Enum.EnumValue "tts.core.package.dataStructures.Enum.EnumValue (Python class) — Represents an individual enum value with its string and integer representation and can be used to access the EnumDefinition.")

- [`Inbox`](#tts.core.package.dataStructures.Inbox.Inbox "tts.core.package.dataStructures.Inbox.Inbox (Python class) — Checks if inbox is empty.")

- [`Map`](#tts.core.package.dataStructures.Map.Map "tts.core.package.dataStructures.Map.Map (Python class) — Two dimensional list of values")

- [`Matrix`](#tts.core.package.dataStructures.Matrix.Matrix "tts.core.package.dataStructures.Matrix.Matrix (Python class) — Two dimensional list of values")

- [`Outbox`](#tts.core.package.dataStructures.Outbox.Outbox "tts.core.package.dataStructures.Outbox.Outbox (Python class) — Sends a message to the connected outbox.")

- [`StructuredSignal`](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignal "tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignal (Python class) — Creates a StructuredSignal if dtype is structured or a StructuredSignalLeaf if dtype is not structured ("flat").")

- [`StructuredSignalLeaf`](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf "tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf (Python class) — Represents a leaf element of a StructuredSignal. Should not be created directly, but by creating a StructuredSignal with a dtype representing a "flat structure".")

- [`Vector`](#tts.core.package.dataStructures.Vector.Vector "tts.core.package.dataStructures.Vector.Vector (Python class) — List of values")

## ByteStream[¶](#bytestream "Link to this heading")

*class* ByteStream[¶](#tts.lib.dataStructures.ByteStream.ByteStream "Link to this definition")  
The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.

This table lists all binary operations on ByteStreams:

| Operation       | Result                              | Example                |
|-----------------|-------------------------------------|------------------------|
| `x | y`| bitwise or of *x* and *y*           | A5:2B | 11:70 = B5:7B |
| `x ^ y`| bitwise exclusive or of *x* and *y* | A5:2B ^ 11:70 = B4:5B  |
| `x & y`| bitwise and of *x* and *y*          | A5:2B & 11:70 = 01:20  |
| `~x`            | the bits of *x* inverted            | ~A5:2B = 5A:D4         |

This table lists all sequence operations on ByteStreams:

| Operation | Result | Example |
|----|----|----|
| `s + t`| the concatenation of *s* and *t* | A5:2B + 11:70 = A5:2B:11:70 |
| `s[i]` | i-th byte of *s* (returns a BitStream) | A5:2B[1] = bits(0x2B, 8) |
| `s[i:j]` | slice of *s* form *i* to *j* | A5:2B:11:70[1:-1] = 2B:11 |
| `len(s)` | length of *s* | len(A5:2B:11:70) = 4 |

This table shows the indexing of bits and bytes in ByteStreams:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| HexValue | 0x | **5B** |  |  |  |  |  |  |  | **C0** |  |  |  |  |  |  |  | … | **67** |  |  |  |  |  |  |  | **2E** |  |  |  |  |  |  |  |
| Byte |  | *0* |  |  |  |  |  |  |  | *1* |  |  |  |  |  |  |  | … | *6* |  |  |  |  |  |  |  | *7* |  |  |  |  |  |  |  |
| BinValue |  | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | … | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 2 | 0 | 1 | 1 | 1 | 0 |
| Bit |  | 7 | … |  |  |  |  |  | 0 | 15 | … |  |  |  |  |  | 8 | … | 55 | … |  |  |  |  |  | 48 | 63 | … |  |  |  |  |  | 56 |

If you want to encode an ascii string as ByteStream or decode a string from ByteStream the following two code snippets might be helpful:

- String to ByteStream: `ByteStream('test'.encode('ascii'))` save as *myByteStream*

- ByteStream to string: `myByteStream.RawString().decode('ascii')` save as *test*

Count(*[otherByteStream](#tts.lib.dataStructures.ByteStream.ByteStream.Count.otherByteStream "tts.lib.dataStructures.ByteStream.ByteStream.Count.otherByteStream (Python parameter) — Searched pattern")*, *[start](#tts.lib.dataStructures.ByteStream.ByteStream.Count "tts.lib.dataStructures.ByteStream.ByteStream.Count.start (Python parameter)")=`0`*, *[end](#tts.lib.dataStructures.ByteStream.ByteStream.Count "tts.lib.dataStructures.ByteStream.ByteStream.Count.end (Python parameter)")=`Ellipsis`*)[¶](#tts.lib.dataStructures.ByteStream.ByteStream.Count "Link to this definition")  
Return the number of occurrences of another ByteStream.

Parameters:  otherByteStream : [ByteStream](#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")[¶](#tts.lib.dataStructures.ByteStream.ByteStream.Count.otherByteStream "Permalink to this definition")  
Searched pattern

Returns:  Number of occurrences

Return type:  int

Find(*[otherByteStream](#tts.lib.dataStructures.ByteStream.ByteStream.Find.otherByteStream "tts.lib.dataStructures.ByteStream.ByteStream.Find.otherByteStream (Python parameter) — Searched pattern")*, *[start](#tts.lib.dataStructures.ByteStream.ByteStream.Find.start "tts.lib.dataStructures.ByteStream.ByteStream.Find.start (Python parameter) — Start byte")=`0`*, *[end](#tts.lib.dataStructures.ByteStream.ByteStream.Find.end "tts.lib.dataStructures.ByteStream.ByteStream.Find.end (Python parameter) — End byte")=`Ellipsis`*)[¶](#tts.lib.dataStructures.ByteStream.ByteStream.Find "Link to this definition")  
Return the lowest index in the ByteStream where another ByteStream is found.

Parameters:  otherByteStream : [ByteStream](#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")[¶](#tts.lib.dataStructures.ByteStream.ByteStream.Find.otherByteStream "Permalink to this definition")  
Searched pattern

start : int[¶](#tts.lib.dataStructures.ByteStream.ByteStream.Find.start "Permalink to this definition")  
Start byte

end : int[¶](#tts.lib.dataStructures.ByteStream.ByteStream.Find.end "Permalink to this definition")  
End byte

Returns:  Index or -1 if not found

Return type:  int

*classmethod* FromIntelWordList(*[wordList](#tts.lib.dataStructures.ByteStream.ByteStream.FromIntelWordList.wordList "tts.lib.dataStructures.ByteStream.ByteStream.FromIntelWordList.wordList (Python parameter) — A list of 16 bit words")*)[¶](#tts.lib.dataStructures.ByteStream.ByteStream.FromIntelWordList "Link to this definition")  
Creates a new ByteStream object from a List of 16 bit words. The bytes are ordered in Intel (little endian) format: 0x1234 becomes 34:12

Parameters:  wordList : list[¶](#tts.lib.dataStructures.ByteStream.ByteStream.FromIntelWordList.wordList "Permalink to this definition")  
A list of 16 bit words

Returns:  A new ByteStream object

Return type:  [ByteStream](#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

*classmethod* FromMotorolaWordList(*[wordList](#tts.lib.dataStructures.ByteStream.ByteStream.FromMotorolaWordList.wordList "tts.lib.dataStructures.ByteStream.ByteStream.FromMotorolaWordList.wordList (Python parameter) — A list of 16 bit words")*)[¶](#tts.lib.dataStructures.ByteStream.ByteStream.FromMotorolaWordList "Link to this definition")  
Creates a new ByteStream object from a List of 16 bit words. The bytes are ordered in Motorola (big endian) format: 0x1234 becomes 12:34

Parameters:  wordList : list[¶](#tts.lib.dataStructures.ByteStream.ByteStream.FromMotorolaWordList.wordList "Permalink to this definition")  
A list of 16 bit words

Returns:  A new ByteStream object

Return type:  [ByteStream](#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

*classmethod* FromRawString(*[rawString](#tts.lib.dataStructures.ByteStream.ByteStream.FromRawString.rawString "tts.lib.dataStructures.ByteStream.ByteStream.FromRawString.rawString (Python parameter) — A bytes object")*)[¶](#tts.lib.dataStructures.ByteStream.ByteStream.FromRawString "Link to this definition")  
Creates a new ByteStream object from a bytes object.

Parameters:  rawString : bytes[¶](#tts.lib.dataStructures.ByteStream.ByteStream.FromRawString.rawString "Permalink to this definition")  
A bytes object

Returns:  A new ByteStream object

Return type:  [ByteStream](#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

HexString()[¶](#tts.lib.dataStructures.ByteStream.ByteStream.HexString "Link to this definition")  
Creates a string representation for this ByteStream. Each byte is displayed as hex number (with leading 0x) and separated by a space.

Returns:  String representation

Return type:  str

IBits(*[startBit](#tts.lib.dataStructures.ByteStream.ByteStream.IBits.startBit "tts.lib.dataStructures.ByteStream.ByteStream.IBits.startBit (Python parameter) — Start bit")=`None`*, *[bitLen](#tts.lib.dataStructures.ByteStream.ByteStream.IBits.bitLen "tts.lib.dataStructures.ByteStream.ByteStream.IBits.bitLen (Python parameter) — Bits")=`None`*)[¶](#tts.lib.dataStructures.ByteStream.ByteStream.IBits "Link to this definition")  
Extracts a BitStream beginning from startBit and with a length of bitLen using Intel byte order.

Parameters:  startBit : int[¶](#tts.lib.dataStructures.ByteStream.ByteStream.IBits.startBit "Permalink to this definition")  
Start bit

bitLen : int[¶](#tts.lib.dataStructures.ByteStream.ByteStream.IBits.bitLen "Permalink to this definition")  
Bits

Returns:  BitStream

Return type:  [BitStream](#tts.lib.dataStructures.BitStream.BitStream "tts.lib.dataStructures.BitStream.BitStream (Python class) — The BitStream type is used to represent binary data. It is possible to represent leading zeros (in contrast to plain integers), as BitStream objects have a defined length. The BitStream type supports binary operations (in contrast to plain strings), sequence operations and checking for equality. When a binary operator has operands with different size, it pads the "shorter" BitStream with zeros until its size matches the size of the "larger" BitStream.")

Index(*[otherByteStream](#tts.lib.dataStructures.ByteStream.ByteStream.Index.otherByteStream "tts.lib.dataStructures.ByteStream.ByteStream.Index.otherByteStream (Python parameter) — Searched pattern")*, *[start](#tts.lib.dataStructures.ByteStream.ByteStream.Index.start "tts.lib.dataStructures.ByteStream.ByteStream.Index.start (Python parameter) — Start byte")=`0`*, *[end](#tts.lib.dataStructures.ByteStream.ByteStream.Index.end "tts.lib.dataStructures.ByteStream.ByteStream.Index.end (Python parameter) — End byte")=`Ellipsis`*)[¶](#tts.lib.dataStructures.ByteStream.ByteStream.Index "Link to this definition")  
Like Find() but raises ValueError if the other ByteStream wasn’t found.

Parameters:  otherByteStream : [ByteStream](#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")[¶](#tts.lib.dataStructures.ByteStream.ByteStream.Index.otherByteStream "Permalink to this definition")  
Searched pattern

start : int[¶](#tts.lib.dataStructures.ByteStream.ByteStream.Index.start "Permalink to this definition")  
Start byte

end : int[¶](#tts.lib.dataStructures.ByteStream.ByteStream.Index.end "Permalink to this definition")  
End byte

Returns:  Index or -1 if not found

Return type:  int

IntelWordList()[¶](#tts.lib.dataStructures.ByteStream.ByteStream.IntelWordList "Link to this definition")  
Creates a word list representation for this Byte Stream, interpreted in Intel (little endian) format. Each pair of bytes is converted to a word: 12:34 becomes 0x3412. The Byte Stream must contain an even number of bytes.

Returns:  Word list representation

Return type:  list

Ints()[¶](#tts.lib.dataStructures.ByteStream.ByteStream.Ints "Link to this definition")  
Converts this ByteStream into a list of positive integers (\<256)

Returns:  List of positive integers

Return type:  list\<int\>

Legacy(*[hexPrefix](#tts.lib.dataStructures.ByteStream.ByteStream.Legacy.hexPrefix "tts.lib.dataStructures.ByteStream.ByteStream.Legacy.hexPrefix (Python parameter) — Enable/disable hex prefix 0x")=`None`*)[¶](#tts.lib.dataStructures.ByteStream.ByteStream.Legacy "Link to this definition")  
Converts this ByteStream into a old-style hex string representation, e.g. “0123affe” or “0x0123affe”

Parameters:  hexPrefix : boolean[¶](#tts.lib.dataStructures.ByteStream.ByteStream.Legacy.hexPrefix "Permalink to this definition")  
Enable/disable hex prefix *0x*

Returns:  Hex string representation

Return type:  str

MBits(*[startBit](#tts.lib.dataStructures.ByteStream.ByteStream.MBits.startBit "tts.lib.dataStructures.ByteStream.ByteStream.MBits.startBit (Python parameter) — Start bit")=`None`*, *[bitLen](#tts.lib.dataStructures.ByteStream.ByteStream.MBits.bitLen "tts.lib.dataStructures.ByteStream.ByteStream.MBits.bitLen (Python parameter) — Bit length")=`None`*)[¶](#tts.lib.dataStructures.ByteStream.ByteStream.MBits "Link to this definition")  
Extracts a BitStream beginning from startBit and with a length of bitLen using Motorola byte order.

Parameters:  startBit : int[¶](#tts.lib.dataStructures.ByteStream.ByteStream.MBits.startBit "Permalink to this definition")  
Start bit

bitLen : int[¶](#tts.lib.dataStructures.ByteStream.ByteStream.MBits.bitLen "Permalink to this definition")  
Bit length

Returns:  BitStream

Return type:  [BitStream](#tts.lib.dataStructures.BitStream.BitStream "tts.lib.dataStructures.BitStream.BitStream (Python class) — The BitStream type is used to represent binary data. It is possible to represent leading zeros (in contrast to plain integers), as BitStream objects have a defined length. The BitStream type supports binary operations (in contrast to plain strings), sequence operations and checking for equality. When a binary operator has operands with different size, it pads the "shorter" BitStream with zeros until its size matches the size of the "larger" BitStream.")

Match(*[expectedPattern](#tts.lib.dataStructures.ByteStream.ByteStream.Match.expectedPattern "tts.lib.dataStructures.ByteStream.ByteStream.Match.expectedPattern (Python parameter) — A string bytestream pattern")*)[¶](#tts.lib.dataStructures.ByteStream.ByteStream.Match "Link to this definition")  
Checks if the given string representation of a bytestream pattern matches this Bytesream.

Allowed wildcard characters for the string bytestream pattern are:

| Wildcard | Description                                 |
|----------|---------------------------------------------|
| `?`      | wildcard character for one half-byte        |
| `*`      | wildcard character for 0..N arbitrary bytes |

| Example                                           | Result |
|---------------------------------------------------|--------|
| ByteStream(“FF:F0:11”).Match(“FF:F0:11”)          | True   |
| ByteStream(“FF:F0:11”).Match(“FF:F0:12”)          | False  |
| ByteStream(“FF:F0:11”).Match(“FF:??:11”)          | True   |
| ByteStream(“FF:A0:10:11”).Match(“F?:A0:?0:\*”)    | True   |
| ByteStream(“FF:F0:01:A9:11”).Match(”\*:01:\*”)    | True   |
| ByteStream(“FF:A0:19:10:11”).Match(“F?:\*:1?:1?”) | True   |
| ByteStream(“FF:A0:29:10”).Match(“F?:\*:1?:??”)    | False  |

Parameters:  expectedPattern : str[¶](#tts.lib.dataStructures.ByteStream.ByteStream.Match.expectedPattern "Permalink to this definition")  
A string bytestream pattern

Returns:  Match Result

Return type:  boolean

MotorolaWordList()[¶](#tts.lib.dataStructures.ByteStream.ByteStream.MotorolaWordList "Link to this definition")  
Creates a word list representation for this Byte Stream, interpreted in Motorola (big endian) format. Each pair of bytes is converted to a word: 12:34 becomes 0x1234 The Byte Stream must contain an even number of bytes.

Returns:  Word list representation

Return type:  list

RawString()[¶](#tts.lib.dataStructures.ByteStream.ByteStream.RawString "Link to this definition")  
Returns the corresponding bytes object for this ByteStream.

Returns:  Bytes object of this ByteStream

Return type:  bytes

Reverse()[¶](#tts.lib.dataStructures.ByteStream.ByteStream.Reverse "Link to this definition")  
Returns a new ByteStream object with its bytes in reversed order.

Returns:  A new ByteStream object

Return type:  [ByteStream](#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

SetIBits(*[startBit](#tts.lib.dataStructures.ByteStream.ByteStream.SetIBits.startBit "tts.lib.dataStructures.ByteStream.ByteStream.SetIBits.startBit (Python parameter) — Start bit")*, *[bits](#tts.lib.dataStructures.ByteStream.ByteStream.SetIBits.bits "tts.lib.dataStructures.ByteStream.ByteStream.SetIBits.bits (Python parameter) — Bits")*)[¶](#tts.lib.dataStructures.ByteStream.ByteStream.SetIBits "Link to this definition")  
Constructs a new ByteStream from this ByteStream, replacing its content from startBit for len(bits) with the content of the BitStream bits using Intel byte order.

Parameters:  startBit : int[¶](#tts.lib.dataStructures.ByteStream.ByteStream.SetIBits.startBit "Permalink to this definition")  
Start bit

bits : [BitStream](#tts.lib.dataStructures.BitStream.BitStream "tts.lib.dataStructures.BitStream.BitStream (Python class) — The BitStream type is used to represent binary data. It is possible to represent leading zeros (in contrast to plain integers), as BitStream objects have a defined length. The BitStream type supports binary operations (in contrast to plain strings), sequence operations and checking for equality. When a binary operator has operands with different size, it pads the "shorter" BitStream with zeros until its size matches the size of the "larger" BitStream.")[¶](#tts.lib.dataStructures.ByteStream.ByteStream.SetIBits.bits "Permalink to this definition")  
Bits

Returns:  A new ByteStream object

Return type:  [ByteStream](#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

SetMBits(*[startBit](#tts.lib.dataStructures.ByteStream.ByteStream.SetMBits.startBit "tts.lib.dataStructures.ByteStream.ByteStream.SetMBits.startBit (Python parameter) — Start bit")*, *[bits](#tts.lib.dataStructures.ByteStream.ByteStream.SetMBits.bits "tts.lib.dataStructures.ByteStream.ByteStream.SetMBits.bits (Python parameter) — BitStream")*)[¶](#tts.lib.dataStructures.ByteStream.ByteStream.SetMBits "Link to this definition")  
Constructs a new ByteStream from this ByteStream, replacing its content from startBit for len(bits) with the content of the BitStream bits using Motorola byte order.

Parameters:  startBit : int[¶](#tts.lib.dataStructures.ByteStream.ByteStream.SetMBits.startBit "Permalink to this definition")  
Start bit

bits : [BitStream](#tts.lib.dataStructures.BitStream.BitStream "tts.lib.dataStructures.BitStream.BitStream (Python class) — The BitStream type is used to represent binary data. It is possible to represent leading zeros (in contrast to plain integers), as BitStream objects have a defined length. The BitStream type supports binary operations (in contrast to plain strings), sequence operations and checking for equality. When a binary operator has operands with different size, it pads the "shorter" BitStream with zeros until its size matches the size of the "larger" BitStream.")[¶](#tts.lib.dataStructures.ByteStream.ByteStream.SetMBits.bits "Permalink to this definition")  
BitStream

Returns:  A new ByteStream object

Return type:  [ByteStream](#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

bsClass[¶](#tts.lib.dataStructures.ByteStream.ByteStream.bsClass "Link to this definition")  
alias of [`BitStream`](#tts.lib.dataStructures.BitStream.BitStream "tts.lib.dataStructures.BitStream.BitStream (Python class) — The BitStream type is used to represent binary data. It is possible to represent leading zeros (in contrast to plain integers), as BitStream objects have a defined length. The BitStream type supports binary operations (in contrast to plain strings), sequence operations and checking for equality. When a binary operator has operands with different size, it pads the "shorter" BitStream with zeros until its size matches the size of the "larger" BitStream.")

## BitStream[¶](#bitstream "Link to this heading")

*class* BitStream[¶](#tts.lib.dataStructures.BitStream.BitStream "Link to this definition")  
The BitStream type is used to represent binary data. It is possible to represent leading zeros (in contrast to plain integers), as BitStream objects have a defined length. The BitStream type supports binary operations (in contrast to plain strings), sequence operations and checking for equality. When a binary operator has operands with different size, it pads the “shorter” BitStream with zeros until its size matches the size of the “larger” BitStream.

*Example usage:*

- `b = BitStream(0, 16)  # a 16-bit BitStream with all zeros: 0000000000000000`- `b = BitStream(0xff, 16)  # a 16-bit BitStream representing 0000000011111111`- `b = BitStream(0xff, 12)  # a 12-bit BitStream representing 000011111111`- `b = BitStream(0b1010, 4)  # a 4-bit BitStream representing 1010`- `b = BitStream([0xff, 0xaa])  # a 16-bit BitStream representing 1111111110101010`- `b = BitStream('ffaa')  # a 16-bit BitStream representing 1111111110101010`This table lists all bit operations on BitStreams:

| Operation | Result | Example |
|----|----|----|
| `x | y`| bitwise or of *x* and *y* | 011001 | 0011 = 011011 |
| `x ^ y`| bitwise exclusive or of *x* and *y* | 011001 ^ 0011 = 011010 |
| `x & y`| bitwise and of *x* and *y* | 011001 & 0011 = 000001 |
| `~x` | the bits of *x* inverted | ~011001 = 100110 |

This table lists all sequence operations on BitStreams:

| Operation | Result | Example |
|----|----|----|
| `s + t`| the concatenation of *s* and *t* | 011001 + 0011 = 0110010011 |
| `s[i]` | i-th bit of *s* (0 is on the right) | 011001[1] = 0 |
| `s[i:j]` | slice of *s* form *i* to *j* | 011001[1:-1] = 1100 |
| `len(s)` | length of *s* | len(011001) = 6 |

Furthermore, there are many methods for BitStream creation, export and manipulation.

This table shows the indexing of bits and bytes in BitStreams:

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| HexValue | 0x | **5B** |  |  |  |  |  |  |  | **C0** |  |  |  |  |  |  |  | … | **67** |  |  |  |  |  |  |  | **2E** |  |  |  |  |  |  |  |
| Byte |  | *0* |  |  |  |  |  |  |  | *1* |  |  |  |  |  |  |  | … | *6* |  |  |  |  |  |  |  | *7* |  |  |  |  |  |  |  |
| BinValue |  | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | … | 0 | 1 | 1 | 0 | 0 | 1 | 1 | 1 | 0 | 0 | 2 | 0 | 1 | 1 | 1 | 0 |
| Bit |  | 63 | … |  |  |  |  |  | 56 | 55 | … |  |  |  |  |  | 48 | … | 15 | … |  |  |  |  |  | 8 | 7 | … |  |  |  |  |  | 0 |

Bin()[¶](#tts.lib.dataStructures.BitStream.BitStream.Bin "Link to this definition")  
Exports this BitStream object as a bit string. This bit string will be a sequence of 0 and 1.

Returns:  bit string representation of this BitStream

Return type:  str

Double()[¶](#tts.lib.dataStructures.BitStream.BitStream.Double "Link to this definition")  
Exports this BitStream object as a float. Raises RuntimeError if the length of this BitStream is not 64.

Returns:  double representation of this BitStream

Return type:  float

Float()[¶](#tts.lib.dataStructures.BitStream.BitStream.Float "Link to this definition")  
Exports this BitStream object as a float. Raises RuntimeError if the length of this BitStream is not 32.

Returns:  float representation of this BitStream

Return type:  float

*classmethod* FromBin(*[value](#tts.lib.dataStructures.BitStream.BitStream.FromBin.value "tts.lib.dataStructures.BitStream.BitStream.FromBin.value (Python parameter) — arbitrary sequence of 0 and 1")*)[¶](#tts.lib.dataStructures.BitStream.BitStream.FromBin "Link to this definition")  
Creates a new BitStream object from a bit string. This string must not contain any character but 0 and 1.

Parameters:  value : str[¶](#tts.lib.dataStructures.BitStream.BitStream.FromBin.value "Permalink to this definition")  
arbitrary sequence of 0 and 1

Returns:  a new BitStream object

Return type:  [BitStream](#tts.lib.dataStructures.BitStream.BitStream "tts.lib.dataStructures.BitStream.BitStream (Python class) — The BitStream type is used to represent binary data. It is possible to represent leading zeros (in contrast to plain integers), as BitStream objects have a defined length. The BitStream type supports binary operations (in contrast to plain strings), sequence operations and checking for equality. When a binary operator has operands with different size, it pads the "shorter" BitStream with zeros until its size matches the size of the "larger" BitStream.")

*classmethod* FromDouble(*[value](#tts.lib.dataStructures.BitStream.BitStream.FromDouble.value "tts.lib.dataStructures.BitStream.BitStream.FromDouble.value (Python parameter) — A Double (64bit)")*)[¶](#tts.lib.dataStructures.BitStream.BitStream.FromDouble "Link to this definition")  
Creates a new BitStream object with a length of 64 from a float.

Parameters:  value : float[¶](#tts.lib.dataStructures.BitStream.BitStream.FromDouble.value "Permalink to this definition")  
A Double (64bit)

Returns:  a new BitStream object

Return type:  [BitStream](#tts.lib.dataStructures.BitStream.BitStream "tts.lib.dataStructures.BitStream.BitStream (Python class) — The BitStream type is used to represent binary data. It is possible to represent leading zeros (in contrast to plain integers), as BitStream objects have a defined length. The BitStream type supports binary operations (in contrast to plain strings), sequence operations and checking for equality. When a binary operator has operands with different size, it pads the "shorter" BitStream with zeros until its size matches the size of the "larger" BitStream.")

*classmethod* FromFloat(*[value](#tts.lib.dataStructures.BitStream.BitStream.FromFloat.value "tts.lib.dataStructures.BitStream.BitStream.FromFloat.value (Python parameter) — A Float (32bit)")*)[¶](#tts.lib.dataStructures.BitStream.BitStream.FromFloat "Link to this definition")  
Creates a new BitStream object with a length of 32 from a float.

Parameters:  value : float[¶](#tts.lib.dataStructures.BitStream.BitStream.FromFloat.value "Permalink to this definition")  
A Float (32bit)

Returns:  a new BitStream object

Return type:  [BitStream](#tts.lib.dataStructures.BitStream.BitStream "tts.lib.dataStructures.BitStream.BitStream (Python class) — The BitStream type is used to represent binary data. It is possible to represent leading zeros (in contrast to plain integers), as BitStream objects have a defined length. The BitStream type supports binary operations (in contrast to plain strings), sequence operations and checking for equality. When a binary operator has operands with different size, it pads the "shorter" BitStream with zeros until its size matches the size of the "larger" BitStream.")

*classmethod* FromInt(*[value](#tts.lib.dataStructures.BitStream.BitStream.FromInt.value "tts.lib.dataStructures.BitStream.BitStream.FromInt.value (Python parameter) — an integer (-(2 ** (length - 1) <= value < 2 ** (length - 1))")*, *[length](#tts.lib.dataStructures.BitStream.BitStream.FromInt.length "tts.lib.dataStructures.BitStream.BitStream.FromInt.length (Python parameter) — length of the resulting BitStream")=`32`*)[¶](#tts.lib.dataStructures.BitStream.BitStream.FromInt "Link to this definition")  
Creates a new BitStream object from an integer (*value*). This integer must be greater than or equal to *-(2 \*\* (length - 1))* and smaller than 2 \*\* (length - 1). Negative numbers are represented using the twos complement.

Parameters:  value : int[¶](#tts.lib.dataStructures.BitStream.BitStream.FromInt.value "Permalink to this definition")  
an integer (-(2 \*\* (length - 1) \<= value \< 2 \*\* (length - 1))

length : int[¶](#tts.lib.dataStructures.BitStream.BitStream.FromInt.length "Permalink to this definition")  
length of the resulting BitStream

Returns:  a new BitStream object

Return type:  [BitStream](#tts.lib.dataStructures.BitStream.BitStream "tts.lib.dataStructures.BitStream.BitStream (Python class) — The BitStream type is used to represent binary data. It is possible to represent leading zeros (in contrast to plain integers), as BitStream objects have a defined length. The BitStream type supports binary operations (in contrast to plain strings), sequence operations and checking for equality. When a binary operator has operands with different size, it pads the "shorter" BitStream with zeros until its size matches the size of the "larger" BitStream.")

*classmethod* FromRawString(*[rawString](#tts.lib.dataStructures.BitStream.BitStream.FromRawString.rawString "tts.lib.dataStructures.BitStream.BitStream.FromRawString.rawString (Python parameter) — a binary string object")*, *[length](#tts.lib.dataStructures.BitStream.BitStream.FromRawString.length "tts.lib.dataStructures.BitStream.BitStream.FromRawString.length (Python parameter) — length of the resulting BitStream")=`None`*)[¶](#tts.lib.dataStructures.BitStream.BitStream.FromRawString "Link to this definition")  
Creates a new BitStream object from a binary string object.

Parameters:  rawString : bytes | bytearray[¶](#tts.lib.dataStructures.BitStream.BitStream.FromRawString.rawString "Permalink to this definition")  
a binary string object

length : int[¶](#tts.lib.dataStructures.BitStream.BitStream.FromRawString.length "Permalink to this definition")  
length of the resulting BitStream

Returns:  a new BitStream object

Return type:  [BitStream](#tts.lib.dataStructures.BitStream.BitStream "tts.lib.dataStructures.BitStream.BitStream (Python class) — The BitStream type is used to represent binary data. It is possible to represent leading zeros (in contrast to plain integers), as BitStream objects have a defined length. The BitStream type supports binary operations (in contrast to plain strings), sequence operations and checking for equality. When a binary operator has operands with different size, it pads the "shorter" BitStream with zeros until its size matches the size of the "larger" BitStream.")

*classmethod* FromUInt(*[value](#tts.lib.dataStructures.BitStream.BitStream.FromUInt.value "tts.lib.dataStructures.BitStream.BitStream.FromUInt.value (Python parameter) — an integer greater than or equal to zero")*, *[length](#tts.lib.dataStructures.BitStream.BitStream.FromUInt.length "tts.lib.dataStructures.BitStream.BitStream.FromUInt.length (Python parameter) — length of the resulting BitStream")=`32`*)[¶](#tts.lib.dataStructures.BitStream.BitStream.FromUInt "Link to this definition")  
Creates a new BitStream object from an integer (*value*). This integer must be greater than or equal to zero and fit into *length* bits.

Parameters:  value : int[¶](#tts.lib.dataStructures.BitStream.BitStream.FromUInt.value "Permalink to this definition")  
an integer greater than or equal to zero

length : int[¶](#tts.lib.dataStructures.BitStream.BitStream.FromUInt.length "Permalink to this definition")  
length of the resulting BitStream

Returns:  a new BitStream object

Return type:  [BitStream](#tts.lib.dataStructures.BitStream.BitStream "tts.lib.dataStructures.BitStream.BitStream (Python class) — The BitStream type is used to represent binary data. It is possible to represent leading zeros (in contrast to plain integers), as BitStream objects have a defined length. The BitStream type supports binary operations (in contrast to plain strings), sequence operations and checking for equality. When a binary operator has operands with different size, it pads the "shorter" BitStream with zeros until its size matches the size of the "larger" BitStream.")

IBytes(*[padding](#tts.lib.dataStructures.BitStream.BitStream.IBytes "tts.lib.dataStructures.BitStream.BitStream.IBytes.padding (Python parameter)")=`0`*)[¶](#tts.lib.dataStructures.BitStream.BitStream.IBytes "Link to this definition")  
Converts this BitStream object (8-bit-padded) in a new ByteStream object using Intel Byteorder.

Returns:  the ByteStream representation of this BitStream using Intel Byteorder

Return type:  [ByteStream](#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

Int()[¶](#tts.lib.dataStructures.BitStream.BitStream.Int "Link to this definition")  
Exports this BitStream object as an integer. This integer will be greater than or equal to *-(2 \*\* (length - 1))* and smaller than 2 \*\* (length - 1). If the MSB is set, this BitStream object will be interpreted as a negative number in twos complement.

Returns:  integer representation of this BitStream

Return type:  [BitStream](#tts.lib.dataStructures.BitStream.BitStream "tts.lib.dataStructures.BitStream.BitStream (Python class) — The BitStream type is used to represent binary data. It is possible to represent leading zeros (in contrast to plain integers), as BitStream objects have a defined length. The BitStream type supports binary operations (in contrast to plain strings), sequence operations and checking for equality. When a binary operator has operands with different size, it pads the "shorter" BitStream with zeros until its size matches the size of the "larger" BitStream.")

MBytes(*[padding](#tts.lib.dataStructures.BitStream.BitStream.MBytes "tts.lib.dataStructures.BitStream.BitStream.MBytes.padding (Python parameter)")=`0`*)[¶](#tts.lib.dataStructures.BitStream.BitStream.MBytes "Link to this definition")  
Converts this BitStream object (8-bit-padded) in a new ByteStream object using Motorola Byteorder.

Returns:  the ByteStream representation of this BitStream using Motorola Byteorder

Return type:  [ByteStream](#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

Pad(*[value](#tts.lib.dataStructures.BitStream.BitStream.Pad.value "tts.lib.dataStructures.BitStream.BitStream.Pad.value (Python parameter) — value used for padding (True or False)")=`None`*, *[multipleOf](#tts.lib.dataStructures.BitStream.BitStream.Pad.multipleOf "tts.lib.dataStructures.BitStream.BitStream.Pad.multipleOf (Python parameter) — multiplier for padding")=`4`*)[¶](#tts.lib.dataStructures.BitStream.BitStream.Pad "Link to this definition")  
Paddes the bitstream with 0’s or 1’s so that its length is a multiple of *multipleOf*.

Parameters:  value : bool[¶](#tts.lib.dataStructures.BitStream.BitStream.Pad.value "Permalink to this definition")  
value used for padding (True or False)

multipleOf : int[¶](#tts.lib.dataStructures.BitStream.BitStream.Pad.multipleOf "Permalink to this definition")  
multiplier for padding

Returns:  a padded copy of this BitStream object

Return type:  [BitStream](#tts.lib.dataStructures.BitStream.BitStream "tts.lib.dataStructures.BitStream.BitStream (Python class) — The BitStream type is used to represent binary data. It is possible to represent leading zeros (in contrast to plain integers), as BitStream objects have a defined length. The BitStream type supports binary operations (in contrast to plain strings), sequence operations and checking for equality. When a binary operator has operands with different size, it pads the "shorter" BitStream with zeros until its size matches the size of the "larger" BitStream.")

Pad4(*[value](#tts.lib.dataStructures.BitStream.BitStream.Pad4 "tts.lib.dataStructures.BitStream.BitStream.Pad4.value (Python parameter)")=`None`*)[¶](#tts.lib.dataStructures.BitStream.BitStream.Pad4 "Link to this definition")  
Equivalent to calling Pad(value, 4)

Pad8(*[value](#tts.lib.dataStructures.BitStream.BitStream.Pad8 "tts.lib.dataStructures.BitStream.BitStream.Pad8.value (Python parameter)")=`None`*)[¶](#tts.lib.dataStructures.BitStream.BitStream.Pad8 "Link to this definition")  
Equivalent to calling Pad(value, 8)

UInt()[¶](#tts.lib.dataStructures.BitStream.BitStream.UInt "Link to this definition")  
Exports this BitStream object as an integer. This integer will be positive (or 0) for any BitStream.

Returns:  integer representation of this BitStream

Return type:  int

bsClass[¶](#tts.lib.dataStructures.BitStream.BitStream.bsClass "Link to this definition")  
alias of [`ByteStream`](#tts.lib.dataStructures.ByteStream.ByteStream "tts.lib.dataStructures.ByteStream.ByteStream (Python class) — The ByteStream type is used to represent byte sequences. The ByteStream type supports binary operations, sequence operations and checking for equality. For binary operations, the operation is applied bytewise. Therefor both operands must be of the same size.")

## Vector[¶](#vector "Link to this heading")

*class* Vector[¶](#tts.core.package.dataStructures.Vector.Vector "Link to this definition")  
Parameters:  iterable : list  
List of values

Creates a Vector object from a given iterable, i.e. a list or tuple.

Example usage: Vector([1,2,3])

GetDimension()[¶](#tts.core.package.dataStructures.Vector.Vector.GetDimension "Link to this definition")  
Returns the length of the vector.

Returns:  dimension

Return type:  int

SetValue(*[x](#tts.core.package.dataStructures.Vector.Vector.SetValue.x "tts.core.package.dataStructures.Vector.Vector.SetValue.x (Python parameter) — index")*, *[value](#tts.core.package.dataStructures.Vector.Vector.SetValue.value "tts.core.package.dataStructures.Vector.Vector.SetValue.value (Python parameter) — value")*)[¶](#tts.core.package.dataStructures.Vector.Vector.SetValue "Link to this definition")  
Sets the value of the given position.

Parameters:  x : int[¶](#tts.core.package.dataStructures.Vector.Vector.SetValue.x "Permalink to this definition")  
index

value : int, float, string, etc.[¶](#tts.core.package.dataStructures.Vector.Vector.SetValue.value "Permalink to this definition")  
value

GetValue(*[x](#tts.core.package.dataStructures.Vector.Vector.GetValue.x "tts.core.package.dataStructures.Vector.Vector.GetValue.x (Python parameter) — index")=`0`*)[¶](#tts.core.package.dataStructures.Vector.Vector.GetValue "Link to this definition")  
Returns the value of the given position.

Parameters:  x : int[¶](#tts.core.package.dataStructures.Vector.Vector.GetValue.x "Permalink to this definition")  
index

Returns:  value

Return type:  int, float, string, etc.

DeleteValue(*[x](#tts.core.package.dataStructures.Vector.Vector.DeleteValue.x "tts.core.package.dataStructures.Vector.Vector.DeleteValue.x (Python parameter) — index")*)[¶](#tts.core.package.dataStructures.Vector.Vector.DeleteValue "Link to this definition")  
Deletes the value of the given position.

Parameters:  x : int[¶](#tts.core.package.dataStructures.Vector.Vector.DeleteValue.x "Permalink to this definition")  
index

List()[¶](#tts.core.package.dataStructures.Vector.Vector.List "Link to this definition")  
Returns a list representation of the Vector.

Returns:  list representation of the Vector

Return type:  list

ToNumpyArray(*[dtype=\<class 'float'\>](#tts.core.package.dataStructures.Vector.Vector.ToNumpyArray "tts.core.package.dataStructures.Vector.Vector.ToNumpyArray.dtype=<class 'float'> (Python parameter)")*)[¶](#tts.core.package.dataStructures.Vector.Vector.ToNumpyArray "Link to this definition")  
Returns a numpy array representation of the Vector.

Parameters:  dtype : see numpy documentation  
data-type

Returns:  numpy array representation of the Vector

Return type:  ndarray

`\_\_add\_\_`(*[toAdd](#tts.core.package.dataStructures.Vector.Vector.__add__ "tts.core.package.dataStructures.Vector.Vector.__add__.toAdd (Python parameter)")*)[¶](#tts.core.package.dataStructures.Vector.Vector.__add__ "Link to this definition")  
This method is called automatically in an expression of the form x+y when x is an instance of this class.

Adds a scalar, a vector or a curve to a vector or a curve. The dimensions in the two latter cases have to be identical. The distribution of a curve is only adopted if the curve is the first operand.

`\_\_sub\_\_`(*[toSub](#tts.core.package.dataStructures.Vector.Vector.__sub__ "tts.core.package.dataStructures.Vector.Vector.__sub__.toSub (Python parameter)")*)[¶](#tts.core.package.dataStructures.Vector.Vector.__sub__ "Link to this definition")  
This method is called automatically in an expression of the form x-y when x is an instance of this class.

Subtracts a scalar, a vector or a curve from a vector or a curve. The dimensions in the two latter cases have to be identical. The distribution of a curve is only adopted if the curve is the first operand.

`\_\_mul\_\_`(*[toMul](#tts.core.package.dataStructures.Vector.Vector.__mul__ "tts.core.package.dataStructures.Vector.Vector.__mul__.toMul (Python parameter)")*)[¶](#tts.core.package.dataStructures.Vector.Vector.__mul__ "Link to this definition")  
This method is called automatically in an expression of the form x\*y when x is an instance of this class.

Multiplies a vector or a curve with a scalar, a vector or a curve. The dimensions in the two latter cases have to be identical. The distribution of a curve is only adopted if the curve is the first operand.

`\_\_truediv\_\_`(*[toDiv](#tts.core.package.dataStructures.Vector.Vector.__truediv__ "tts.core.package.dataStructures.Vector.Vector.__truediv__.toDiv (Python parameter)")*)[¶](#tts.core.package.dataStructures.Vector.Vector.__truediv__ "Link to this definition")  
This method is called automatically in an expression of the form x/y when x is an instance of this class.

Divides a vector or a curve by a scalar, a vector or a curve. The dimensions in the two latter cases have to be identical. The distribution of a curve is only adopted if the curve is the first operand.

## Matrix[¶](#matrix "Link to this heading")

*class* Matrix[¶](#tts.core.package.dataStructures.Matrix.Matrix "Link to this definition")  
Parameters:  iterable : list  
Two dimensional list of values

Creates a Matrix object from a given two dimensional iterable, i.e. a nested list. Matrices are stored in the column layout. This entails that to index a matrix variable, the column is specified first and subsequently the row.

Example usage: Matrix([[1,2,3],[11,22,33]]), creates a matrix with two columns and three rows.

GetXDimension()[¶](#tts.core.package.dataStructures.Matrix.Matrix.GetXDimension "Link to this definition")  
Returns the dimension of x.

Returns:  dimension

Return type:  int

GetYDimension()[¶](#tts.core.package.dataStructures.Matrix.Matrix.GetYDimension "Link to this definition")  
Returns the dimension of y.

Returns:  dimension

Return type:  int

GetValue(*[x](#tts.core.package.dataStructures.Matrix.Matrix.GetValue.x "tts.core.package.dataStructures.Matrix.Matrix.GetValue.x (Python parameter) — index x")*, *[y](#tts.core.package.dataStructures.Matrix.Matrix.GetValue.y "tts.core.package.dataStructures.Matrix.Matrix.GetValue.y (Python parameter) — index y")*)[¶](#tts.core.package.dataStructures.Matrix.Matrix.GetValue "Link to this definition")  
Returns the value of the given position.

Parameters:  x : int[¶](#tts.core.package.dataStructures.Matrix.Matrix.GetValue.x "Permalink to this definition")  
index x

y : int[¶](#tts.core.package.dataStructures.Matrix.Matrix.GetValue.y "Permalink to this definition")  
index y

Returns:  value

Return type:  float

SetValue(*[x](#tts.core.package.dataStructures.Matrix.Matrix.SetValue.x "tts.core.package.dataStructures.Matrix.Matrix.SetValue.x (Python parameter) — index x")*, *[y](#tts.core.package.dataStructures.Matrix.Matrix.SetValue.y "tts.core.package.dataStructures.Matrix.Matrix.SetValue.y (Python parameter) — index y")*, *[value](#tts.core.package.dataStructures.Matrix.Matrix.SetValue.value "tts.core.package.dataStructures.Matrix.Matrix.SetValue.value (Python parameter) — value")*)[¶](#tts.core.package.dataStructures.Matrix.Matrix.SetValue "Link to this definition")  
Sets the value of the given position.

Parameters:  x : int[¶](#tts.core.package.dataStructures.Matrix.Matrix.SetValue.x "Permalink to this definition")  
index x

y : int[¶](#tts.core.package.dataStructures.Matrix.Matrix.SetValue.y "Permalink to this definition")  
index y

value : any[¶](#tts.core.package.dataStructures.Matrix.Matrix.SetValue.value "Permalink to this definition")  
value

DeleteValue(*[x](#tts.core.package.dataStructures.Matrix.Matrix.DeleteValue.x "tts.core.package.dataStructures.Matrix.Matrix.DeleteValue.x (Python parameter) — index x")*, *[y](#tts.core.package.dataStructures.Matrix.Matrix.DeleteValue.y "tts.core.package.dataStructures.Matrix.Matrix.DeleteValue.y (Python parameter) — index y")*)[¶](#tts.core.package.dataStructures.Matrix.Matrix.DeleteValue "Link to this definition")  
Deletes the value of the given position.

Parameters:  x : int[¶](#tts.core.package.dataStructures.Matrix.Matrix.DeleteValue.x "Permalink to this definition")  
index x

y : int[¶](#tts.core.package.dataStructures.Matrix.Matrix.DeleteValue.y "Permalink to this definition")  
index y

GetRow(*[y](#tts.core.package.dataStructures.Matrix.Matrix.GetRow.y "tts.core.package.dataStructures.Matrix.Matrix.GetRow.y (Python parameter) — row")*)[¶](#tts.core.package.dataStructures.Matrix.Matrix.GetRow "Link to this definition")  
Returns the row of the given index.

Parameters:  y : int[¶](#tts.core.package.dataStructures.Matrix.Matrix.GetRow.y "Permalink to this definition")  
row

Returns:  row as a list of the values

Return type:  list

GetCol(*[x](#tts.core.package.dataStructures.Matrix.Matrix.GetCol.x "tts.core.package.dataStructures.Matrix.Matrix.GetCol.x (Python parameter) — column")*)[¶](#tts.core.package.dataStructures.Matrix.Matrix.GetCol "Link to this definition")  
Returns the column of the given index.

Parameters:  x : int[¶](#tts.core.package.dataStructures.Matrix.Matrix.GetCol.x "Permalink to this definition")  
column

Returns:  column as a list of the values

Return type:  list

List()[¶](#tts.core.package.dataStructures.Matrix.Matrix.List "Link to this definition")  
Returns a two-dimensional list representation of the matrix.

Returns:  list representation of the matrix

Return type:  list

ToNumpyArray(*[dtype=\<class 'float'\>](#tts.core.package.dataStructures.Matrix.Matrix.ToNumpyArray "tts.core.package.dataStructures.Matrix.Matrix.ToNumpyArray.dtype=<class 'float'> (Python parameter)")*)[¶](#tts.core.package.dataStructures.Matrix.Matrix.ToNumpyArray "Link to this definition")  
Returns a two-dimensional numpy array representation of the matrix.

Parameters:  dtype : see numpy documentation  
data-type

Returns:  numpy array representation of the matrix

Return type:  ndarray

`\_\_add\_\_`(*[toAdd](#tts.core.package.dataStructures.Matrix.Matrix.__add__ "tts.core.package.dataStructures.Matrix.Matrix.__add__.toAdd (Python parameter)")*)[¶](#tts.core.package.dataStructures.Matrix.Matrix.__add__ "Link to this definition")  
This method is called automatically in an expression of the form x+y when x is an instance of this class.

Adds a scalar, a matrix or a map to a matrix or a map. The dimensions in the two latter cases have to be identical. The distributions of a map are only adopted if the map is the first operand.

`\_\_sub\_\_`(*[toSub](#tts.core.package.dataStructures.Matrix.Matrix.__sub__ "tts.core.package.dataStructures.Matrix.Matrix.__sub__.toSub (Python parameter)")*)[¶](#tts.core.package.dataStructures.Matrix.Matrix.__sub__ "Link to this definition")  
This method is called automatically in an expression of the form x-y when x is an instance of this class.

Subtracts a scalar, a matrix or a map from a matrix or a map. The dimensions in the two latter cases have to be identical. The distributions of a map are only adopted if the map is the first operand.

`\_\_mul\_\_`(*[toMul](#tts.core.package.dataStructures.Matrix.Matrix.__mul__ "tts.core.package.dataStructures.Matrix.Matrix.__mul__.toMul (Python parameter)")*)[¶](#tts.core.package.dataStructures.Matrix.Matrix.__mul__ "Link to this definition")  
This method is called automatically in an expression of the form x\*y when x is an instance of this class.

Multiplies a matrix or a map with a scalar, a matrix or a map. The dimensions in the two latter cases have to be identical. The distributions of a map are only adopted if the map is the first operand.

`\_\_truediv\_\_`(*[toDiv](#tts.core.package.dataStructures.Matrix.Matrix.__truediv__ "tts.core.package.dataStructures.Matrix.Matrix.__truediv__.toDiv (Python parameter)")*)[¶](#tts.core.package.dataStructures.Matrix.Matrix.__truediv__ "Link to this definition")  
This method is called automatically in an expression of the form x/y when x is an instance of this class.

Divides a matrix or a map by a scalar, a matrix or a map. The dimensions in the two latter cases have to be identical. The distributions of a map are only adopted if the map is the first operand.

## Curve[¶](#curve "Link to this heading")

*class* Curve[¶](#tts.core.package.dataStructures.Curve.Curve "Link to this definition")  
Parameters:  values : list  
List of values

distribution : list  
List of distribution

Creates a curve from 2 iterables representing the values and the distribution which may be lists, tuples or vectors, respectively.

Example usage: Curve([1,2,3],[11,22,33])

SetDistributionValue(*[x](#tts.core.package.dataStructures.Curve.Curve.SetDistributionValue.x "tts.core.package.dataStructures.Curve.Curve.SetDistributionValue.x (Python parameter) — index")*, *[value](#tts.core.package.dataStructures.Curve.Curve.SetDistributionValue.value "tts.core.package.dataStructures.Curve.Curve.SetDistributionValue.value (Python parameter) — distribution level value")*)[¶](#tts.core.package.dataStructures.Curve.Curve.SetDistributionValue "Link to this definition")  
Sets the distribution level of the given position.

Parameters:  x : int[¶](#tts.core.package.dataStructures.Curve.Curve.SetDistributionValue.x "Permalink to this definition")  
index

value : [Expression](ExpressionApi/Expression.md#ApiClient.Expression "ApiClient.Expression (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")[¶](#tts.core.package.dataStructures.Curve.Curve.SetDistributionValue.value "Permalink to this definition")  
distribution level value

GetDistributionValue(*[x](#tts.core.package.dataStructures.Curve.Curve.GetDistributionValue.x "tts.core.package.dataStructures.Curve.Curve.GetDistributionValue.x (Python parameter) — index")*)[¶](#tts.core.package.dataStructures.Curve.Curve.GetDistributionValue "Link to this definition")  
Gets the distribution level of the given position.

Parameters:  x : int[¶](#tts.core.package.dataStructures.Curve.Curve.GetDistributionValue.x "Permalink to this definition")  
index

Returns:  distribution level value

Return type:  [Expression](ExpressionApi/Expression.md#ApiClient.Expression "ApiClient.Expression (Python class) — Call this method if you want to use API-objects in multiple contexts, e.g. if you want to insert a specific test step in multiple blocks.")

DeleteDistributionValue(*[x](#tts.core.package.dataStructures.Curve.Curve.DeleteDistributionValue.x "tts.core.package.dataStructures.Curve.Curve.DeleteDistributionValue.x (Python parameter) — index")*)[¶](#tts.core.package.dataStructures.Curve.Curve.DeleteDistributionValue "Link to this definition")  
Deletes the distribution level of the given position.

Parameters:  x : int[¶](#tts.core.package.dataStructures.Curve.Curve.DeleteDistributionValue.x "Permalink to this definition")  
index

GetDistribution()[¶](#tts.core.package.dataStructures.Curve.Curve.GetDistribution "Link to this definition")  
Returns the distribution vector.

Returns:  distribution vector

Return type:  [Vector](#tts.core.package.dataStructures.Vector.Vector "tts.core.package.dataStructures.Vector.Vector (Python class) — List of values")

List()[¶](#tts.core.package.dataStructures.Curve.Curve.List "Link to this definition")  
Returns a list representation of the values of the curve.

Returns:  list representation of the values of the curve

Return type:  list

Interpolate(*[xCoord](#tts.core.package.dataStructures.Curve.Curve.Interpolate.xCoord "tts.core.package.dataStructures.Curve.Curve.Interpolate.xCoord (Python parameter) — coordinate x")*)[¶](#tts.core.package.dataStructures.Curve.Curve.Interpolate "Link to this definition")  
Calculates the value for a given x coordinate by means of linear interpolation.

In order to use a custom interpolation, you can retrieve the axis as a [`Vector`](#tts.core.package.dataStructures.Vector.Vector "tts.core.package.dataStructures.Vector.Vector (Python class) — List of values") via [`GetDistribution()`](#tts.core.package.dataStructures.Curve.Curve.GetDistribution "tts.core.package.dataStructures.Curve.Curve.GetDistribution (Python method) — Returns the distribution vector.") and call [`ToNumpyArray()`](#tts.core.package.dataStructures.Curve.Curve.ToNumpyArray "tts.core.package.dataStructures.Curve.Curve.ToNumpyArray (Python method) — Returns a numpy array representation of the Vector.") both on the axis and on the Curve object itself (for the z vector) to obtain numpy arrays.

Parameters:  xCoord : float[¶](#tts.core.package.dataStructures.Curve.Curve.Interpolate.xCoord "Permalink to this definition")  
coordinate x

Returns:  interpolated value

Return type:  float

GetDimension()[¶](#tts.core.package.dataStructures.Curve.Curve.GetDimension "Link to this definition")  
Returns the length of the vector.

Returns:  dimension

Return type:  int

GetValue(*[x](#tts.core.package.dataStructures.Curve.Curve.GetValue.x "tts.core.package.dataStructures.Curve.Curve.GetValue.x (Python parameter) — index")=`0`*)[¶](#tts.core.package.dataStructures.Curve.Curve.GetValue "Link to this definition")  
Returns the value of the given position.

Parameters:  x : int[¶](#tts.core.package.dataStructures.Curve.Curve.GetValue.x "Permalink to this definition")  
index

Returns:  value

Return type:  int, float, string, etc.

SetValue(*[x](#tts.core.package.dataStructures.Curve.Curve.SetValue.x "tts.core.package.dataStructures.Curve.Curve.SetValue.x (Python parameter) — index")*, *[value](#tts.core.package.dataStructures.Curve.Curve.SetValue.value "tts.core.package.dataStructures.Curve.Curve.SetValue.value (Python parameter) — value")*)[¶](#tts.core.package.dataStructures.Curve.Curve.SetValue "Link to this definition")  
Sets the value of the given position.

Parameters:  x : int[¶](#tts.core.package.dataStructures.Curve.Curve.SetValue.x "Permalink to this definition")  
index

value : int, float, string, etc.[¶](#tts.core.package.dataStructures.Curve.Curve.SetValue.value "Permalink to this definition")  
value

ToNumpyArray(*[dtype=\<class 'float'\>](#tts.core.package.dataStructures.Curve.Curve.ToNumpyArray "tts.core.package.dataStructures.Curve.Curve.ToNumpyArray.dtype=<class 'float'> (Python parameter)")*)[¶](#tts.core.package.dataStructures.Curve.Curve.ToNumpyArray "Link to this definition")  
Returns a numpy array representation of the Vector.

Parameters:  dtype : see numpy documentation  
data-type

Returns:  numpy array representation of the Vector

Return type:  ndarray

## EnumDefinition[¶](#enumdefinition "Link to this heading")

*class* EnumDefinition[¶](#tts.core.package.dataStructures.Enum.EnumDefinition "Link to this definition")  
Is returned when accessing the attribute enum of an [`EnumValue`](#tts.core.package.dataStructures.Enum.EnumValue "tts.core.package.dataStructures.Enum.EnumValue (Python class) — Represents an individual enum value with its string and integer representation and can be used to access the EnumDefinition.").

`\_\_iter\_\_`()[¶](#tts.core.package.dataStructures.Enum.EnumDefinition.__iter__ "Link to this definition")  
Iterator over the [`EnumValue`](#tts.core.package.dataStructures.Enum.EnumValue "tts.core.package.dataStructures.Enum.EnumValue (Python class) — Represents an individual enum value with its string and integer representation and can be used to access the EnumDefinition.") objects of the [`EnumDefinition`](#tts.core.package.dataStructures.Enum.EnumDefinition "tts.core.package.dataStructures.Enum.EnumDefinition (Python class) — Is returned when accessing the attribute enum of an EnumValue.").

`\_\_getattr\_\_`(*[item](#tts.core.package.dataStructures.Enum.EnumDefinition.__getattr__.item "tts.core.package.dataStructures.Enum.EnumDefinition.__getattr__.item (Python parameter) — Some string Enum value")*)[¶](#tts.core.package.dataStructures.Enum.EnumDefinition.__getattr__ "Link to this definition")  
Flexible access of [`EnumValue`](#tts.core.package.dataStructures.Enum.EnumValue "tts.core.package.dataStructures.Enum.EnumValue (Python class) — Represents an individual enum value with its string and integer representation and can be used to access the EnumDefinition.")

- `myEnumDef.strName`

- `myEnumDef.enum.strName`

The returning [`EnumValue`](#tts.core.package.dataStructures.Enum.EnumValue "tts.core.package.dataStructures.Enum.EnumValue (Python class) — Represents an individual enum value with its string and integer representation and can be used to access the EnumDefinition.") is initialized with the corresponding int value of the string value and does not hold an [`EnumDefinition`](#tts.core.package.dataStructures.Enum.EnumDefinition "tts.core.package.dataStructures.Enum.EnumDefinition (Python class) — Is returned when accessing the attribute enum of an EnumValue."). Therefore, second access of the enum-attribute from the EnumValue is not possible (no recursion possible).

- not possible: `myEnumDef.enum.strName.enum`

Parameters:  item : str[¶](#tts.core.package.dataStructures.Enum.EnumDefinition.__getattr__.item "Permalink to this definition")  
Some string Enum value

Returns:  [`EnumValue`](#tts.core.package.dataStructures.Enum.EnumValue "tts.core.package.dataStructures.Enum.EnumValue (Python class) — Represents an individual enum value with its string and integer representation and can be used to access the EnumDefinition.") initialized with int

Raises:  
AttributeError. Otherwise, the builtin function `getattr(enumDef,'strVal', None)`does not work .

Return type:  [*EnumValue*](#tts.core.package.dataStructures.Enum.EnumValue "tts.core.package.dataStructures.Enum.EnumValue (Python class) — Represents an individual enum value with its string and integer representation and can be used to access the EnumDefinition.")

`\_\_getitem\_\_`(*[item](#tts.core.package.dataStructures.Enum.EnumDefinition.__getitem__.item "tts.core.package.dataStructures.Enum.EnumDefinition.__getitem__.item (Python parameter) — Some string Enum value (with possible white spaces)")*)[¶](#tts.core.package.dataStructures.Enum.EnumDefinition.__getitem__ "Link to this definition")  
Flexible access of [`EnumValue`](#tts.core.package.dataStructures.Enum.EnumValue "tts.core.package.dataStructures.Enum.EnumValue (Python class) — Represents an individual enum value with its string and integer representation and can be used to access the EnumDefinition.")

- `myEnumDef['strName']`

- `myEnumDef.enum['strName']`

The returning [`EnumValue`](#tts.core.package.dataStructures.Enum.EnumValue "tts.core.package.dataStructures.Enum.EnumValue (Python class) — Represents an individual enum value with its string and integer representation and can be used to access the EnumDefinition.") is initialized with the corresponding int value of the string value and does not hold an [`EnumDefinition`](#tts.core.package.dataStructures.Enum.EnumDefinition "tts.core.package.dataStructures.Enum.EnumDefinition (Python class) — Is returned when accessing the attribute enum of an EnumValue."). Therefore, second access of the enum-attribute from the [`EnumValue`](#tts.core.package.dataStructures.Enum.EnumValue "tts.core.package.dataStructures.Enum.EnumValue (Python class) — Represents an individual enum value with its string and integer representation and can be used to access the EnumDefinition.") is not possible (no recursion possible).

- not possible: `myEnumDef.enum.strName.enum`

Parameters:  item : str[¶](#tts.core.package.dataStructures.Enum.EnumDefinition.__getitem__.item "Permalink to this definition")  
Some string Enum value (with possible white spaces)

Returns:  [`EnumValue`](#tts.core.package.dataStructures.Enum.EnumValue "tts.core.package.dataStructures.Enum.EnumValue (Python class) — Represents an individual enum value with its string and integer representation and can be used to access the EnumDefinition.") initialized with int

Return type:  [*EnumValue*](#tts.core.package.dataStructures.Enum.EnumValue "tts.core.package.dataStructures.Enum.EnumValue (Python class) — Represents an individual enum value with its string and integer representation and can be used to access the EnumDefinition.")

## EnumValue[¶](#enumvalue "Link to this heading")

*class* EnumValue[¶](#tts.core.package.dataStructures.Enum.EnumValue "Link to this definition")  
Represents an individual enum value with its string and integer representation and can be used to access the [`EnumDefinition`](#tts.core.package.dataStructures.Enum.EnumDefinition "tts.core.package.dataStructures.Enum.EnumDefinition (Python class) — Is returned when accessing the attribute enum of an EnumValue.").

`\_\_eq\_\_`(*[other](#tts.core.package.dataStructures.Enum.EnumValue.__eq__.other "tts.core.package.dataStructures.Enum.EnumValue.__eq__.other (Python parameter) — str or int value of the EnumValue to compare with")*)[¶](#tts.core.package.dataStructures.Enum.EnumValue.__eq__ "Link to this definition")  
[`EnumValue`](#tts.core.package.dataStructures.Enum.EnumValue "tts.core.package.dataStructures.Enum.EnumValue (Python class) — Represents an individual enum value with its string and integer representation and can be used to access the EnumDefinition.") is compared flexibly to either str or int.

Parameters:  other : str or int[¶](#tts.core.package.dataStructures.Enum.EnumValue.__eq__.other "Permalink to this definition")  
str or int value of the [`EnumValue`](#tts.core.package.dataStructures.Enum.EnumValue "tts.core.package.dataStructures.Enum.EnumValue (Python class) — Represents an individual enum value with its string and integer representation and can be used to access the EnumDefinition.") to compare with

int[¶](#tts.core.package.dataStructures.Enum.EnumValue.int "Link to this definition")  
Returns:  Numerical representation of the [`EnumValue`](#tts.core.package.dataStructures.Enum.EnumValue "tts.core.package.dataStructures.Enum.EnumValue (Python class) — Represents an individual enum value with its string and integer representation and can be used to access the EnumDefinition.").

str[¶](#tts.core.package.dataStructures.Enum.EnumValue.str "Link to this definition")  
Returns:  Textual representation of the [`EnumValue`](#tts.core.package.dataStructures.Enum.EnumValue "tts.core.package.dataStructures.Enum.EnumValue (Python class) — Represents an individual enum value with its string and integer representation and can be used to access the EnumDefinition.").

enum[¶](#tts.core.package.dataStructures.Enum.EnumValue.enum "Link to this definition")  
Returns:  The [`EnumDefinition`](#tts.core.package.dataStructures.Enum.EnumDefinition "tts.core.package.dataStructures.Enum.EnumDefinition (Python class) — Is returned when accessing the attribute enum of an EnumValue.") which corresponds to the [`EnumValue`](#tts.core.package.dataStructures.Enum.EnumValue "tts.core.package.dataStructures.Enum.EnumValue (Python class) — Represents an individual enum value with its string and integer representation and can be used to access the EnumDefinition.").

Exception:  
AttributeError

## Map[¶](#map "Link to this heading")

*class* Map[¶](#tts.core.package.dataStructures.Map.Map "Link to this definition")  
Parameters:  values : list  
Two dimensional list of values

xDistribution : list  
List of X distribution

yDistribution : list  
List of Y distribution

Creates a Map from a given Matrix or nested two dimensional list/tuple with distributions from given vectors or one dimensional list/tuples.

Example usage: Map([[1,2,3],[6,7,8]], [11,22], [12,13,14])

GetXDistribution()[¶](#tts.core.package.dataStructures.Map.Map.GetXDistribution "Link to this definition")  
Returns the X distribution vector.

Returns:  X distribution vector

Return type:  [Vector](#tts.core.package.dataStructures.Vector.Vector "tts.core.package.dataStructures.Vector.Vector (Python class) — List of values")

GetYDistribution()[¶](#tts.core.package.dataStructures.Map.Map.GetYDistribution "Link to this definition")  
Returns the X distribution vector.

Returns:  X distribution vector

Return type:  [Vector](#tts.core.package.dataStructures.Vector.Vector "tts.core.package.dataStructures.Vector.Vector (Python class) — List of values")

GetXDistributionValue(*[x](#tts.core.package.dataStructures.Map.Map.GetXDistributionValue.x "tts.core.package.dataStructures.Map.Map.GetXDistributionValue.x (Python parameter) — index")*)[¶](#tts.core.package.dataStructures.Map.Map.GetXDistributionValue "Link to this definition")  
Gets the x-distribution level of the given position.

Parameters:  x : int[¶](#tts.core.package.dataStructures.Map.Map.GetXDistributionValue.x "Permalink to this definition")  
index

Returns:  x-distribution level value

Return type:  any

DeleteXDistributionValue(*[x](#tts.core.package.dataStructures.Map.Map.DeleteXDistributionValue.x "tts.core.package.dataStructures.Map.Map.DeleteXDistributionValue.x (Python parameter) — index")*)[¶](#tts.core.package.dataStructures.Map.Map.DeleteXDistributionValue "Link to this definition")  
Deletes the x-distribution level of the given position.

Parameters:  x : any[¶](#tts.core.package.dataStructures.Map.Map.DeleteXDistributionValue.x "Permalink to this definition")  
index

GetYDistributionValue(*[y](#tts.core.package.dataStructures.Map.Map.GetYDistributionValue.y "tts.core.package.dataStructures.Map.Map.GetYDistributionValue.y (Python parameter) — index")*)[¶](#tts.core.package.dataStructures.Map.Map.GetYDistributionValue "Link to this definition")  
Gets the y-distribution level of the given position.

Parameters:  y : int[¶](#tts.core.package.dataStructures.Map.Map.GetYDistributionValue.y "Permalink to this definition")  
index

Returns:  y-distribution level value

Return type:  any

DeleteYDistributionValue(*[y](#tts.core.package.dataStructures.Map.Map.DeleteYDistributionValue.y "tts.core.package.dataStructures.Map.Map.DeleteYDistributionValue.y (Python parameter) — index")*)[¶](#tts.core.package.dataStructures.Map.Map.DeleteYDistributionValue "Link to this definition")  
Deletes the y-distribution level of the given position.

Parameters:  y : int[¶](#tts.core.package.dataStructures.Map.Map.DeleteYDistributionValue.y "Permalink to this definition")  
index

SetXDistributionValue(*[x](#tts.core.package.dataStructures.Map.Map.SetXDistributionValue.x "tts.core.package.dataStructures.Map.Map.SetXDistributionValue.x (Python parameter) — index")*, *[value](#tts.core.package.dataStructures.Map.Map.SetXDistributionValue.value "tts.core.package.dataStructures.Map.Map.SetXDistributionValue.value (Python parameter) — x-distribution level value")*)[¶](#tts.core.package.dataStructures.Map.Map.SetXDistributionValue "Link to this definition")  
Sets the x-distribution level of the given position.

Parameters:  x : int[¶](#tts.core.package.dataStructures.Map.Map.SetXDistributionValue.x "Permalink to this definition")  
index

value : any[¶](#tts.core.package.dataStructures.Map.Map.SetXDistributionValue.value "Permalink to this definition")  
x-distribution level value

SetYDistributionValue(*[y](#tts.core.package.dataStructures.Map.Map.SetYDistributionValue.y "tts.core.package.dataStructures.Map.Map.SetYDistributionValue.y (Python parameter) — index")*, *[value](#tts.core.package.dataStructures.Map.Map.SetYDistributionValue.value "tts.core.package.dataStructures.Map.Map.SetYDistributionValue.value (Python parameter) — y-distribution level value")*)[¶](#tts.core.package.dataStructures.Map.Map.SetYDistributionValue "Link to this definition")  
Sets the x-distribution level of the given position.

Parameters:  y : int[¶](#tts.core.package.dataStructures.Map.Map.SetYDistributionValue.y "Permalink to this definition")  
index

value : any[¶](#tts.core.package.dataStructures.Map.Map.SetYDistributionValue.value "Permalink to this definition")  
y-distribution level value

List()[¶](#tts.core.package.dataStructures.Map.Map.List "Link to this definition")  
Returns a two dimensional list representation of the values of the map.

Returns:  list representation of the values of the map

Return type:  list

Interpolate(*[xCoord](#tts.core.package.dataStructures.Map.Map.Interpolate.xCoord "tts.core.package.dataStructures.Map.Map.Interpolate.xCoord (Python parameter) — x coordiate")*, *[yCoord](#tts.core.package.dataStructures.Map.Map.Interpolate.yCoord "tts.core.package.dataStructures.Map.Map.Interpolate.yCoord (Python parameter) — y coordinate")*)[¶](#tts.core.package.dataStructures.Map.Map.Interpolate "Link to this definition")  
Calculates the value of a given pair of coordinates by means of linear interpolation, first along the x axis and then along the y axis.

In order to use a custom interpolation, you can retrieve the x axis and y axis as Vectors via [`GetXDistribution()`](#tts.core.package.dataStructures.Map.Map.GetXDistribution "tts.core.package.dataStructures.Map.Map.GetXDistribution (Python method) — Returns the X distribution vector.") and [`GetYDistribution()`](#tts.core.package.dataStructures.Map.Map.GetYDistribution "tts.core.package.dataStructures.Map.Map.GetYDistribution (Python method) — Returns the X distribution vector."), and call [`ToNumpyArray()`](#tts.core.package.dataStructures.Vector.Vector.ToNumpyArray "tts.core.package.dataStructures.Vector.Vector.ToNumpyArray (Python method) — Returns a numpy array representation of the Vector.") on both axes as well as [`ToNumpyArray()`](#tts.core.package.dataStructures.Matrix.Matrix.ToNumpyArray "tts.core.package.dataStructures.Matrix.Matrix.ToNumpyArray (Python method) — Returns a two-dimensional numpy array representation of the matrix.") on the Map object itself (for the z matrix) to obtain numpy arrays.

Parameters:  xCoord : float[¶](#tts.core.package.dataStructures.Map.Map.Interpolate.xCoord "Permalink to this definition")  
x coordiate

yCoord : float[¶](#tts.core.package.dataStructures.Map.Map.Interpolate.yCoord "Permalink to this definition")  
y coordinate

Returns:  interpolated value

Return type:  float

GetXDimension()[¶](#tts.core.package.dataStructures.Map.Map.GetXDimension "Link to this definition")  
Returns the dimension of x.

Returns:  dimension

Return type:  int

GetYDimension()[¶](#tts.core.package.dataStructures.Map.Map.GetYDimension "Link to this definition")  
Returns the dimension of y.

Returns:  dimension

Return type:  int

GetValue(*[x](#tts.core.package.dataStructures.Map.Map.GetValue.x "tts.core.package.dataStructures.Map.Map.GetValue.x (Python parameter) — index x")*, *[y](#tts.core.package.dataStructures.Map.Map.GetValue.y "tts.core.package.dataStructures.Map.Map.GetValue.y (Python parameter) — index y")*)[¶](#tts.core.package.dataStructures.Map.Map.GetValue "Link to this definition")  
Returns the value of the given position.

Parameters:  x : int[¶](#tts.core.package.dataStructures.Map.Map.GetValue.x "Permalink to this definition")  
index x

y : int[¶](#tts.core.package.dataStructures.Map.Map.GetValue.y "Permalink to this definition")  
index y

Returns:  value

Return type:  float

SetValue(*[x](#tts.core.package.dataStructures.Map.Map.SetValue.x "tts.core.package.dataStructures.Map.Map.SetValue.x (Python parameter) — index x")*, *[y](#tts.core.package.dataStructures.Map.Map.SetValue.y "tts.core.package.dataStructures.Map.Map.SetValue.y (Python parameter) — index y")*, *[value](#tts.core.package.dataStructures.Map.Map.SetValue.value "tts.core.package.dataStructures.Map.Map.SetValue.value (Python parameter) — value")*)[¶](#tts.core.package.dataStructures.Map.Map.SetValue "Link to this definition")  
Sets the value of the given position.

Parameters:  x : int[¶](#tts.core.package.dataStructures.Map.Map.SetValue.x "Permalink to this definition")  
index x

y : int[¶](#tts.core.package.dataStructures.Map.Map.SetValue.y "Permalink to this definition")  
index y

value : any[¶](#tts.core.package.dataStructures.Map.Map.SetValue.value "Permalink to this definition")  
value

ToNumpyArray(*[dtype=\<class 'float'\>](#tts.core.package.dataStructures.Map.Map.ToNumpyArray "tts.core.package.dataStructures.Map.Map.ToNumpyArray.dtype=<class 'float'> (Python parameter)")*)[¶](#tts.core.package.dataStructures.Map.Map.ToNumpyArray "Link to this definition")  
Returns a two-dimensional numpy array representation of the matrix.

Parameters:  dtype : see numpy documentation  
data-type

Returns:  numpy array representation of the matrix

Return type:  ndarray

## StructuredSignal[¶](#structuredsignal "Link to this heading")

*class* StructuredSignal[¶](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignal "Link to this definition")  
Creates a [`StructuredSignal`](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignal "tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignal (Python class) — Creates a StructuredSignal if dtype is structured or a StructuredSignalLeaf if dtype is not structured ("flat").") if dtype is structured or a [`StructuredSignalLeaf`](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf "tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf (Python class) — Represents a leaf element of a StructuredSignal. Should not be created directly, but by creating a StructuredSignal with a dtype representing a "flat structure".") if dtype is not structured (“flat”).

Parameters:  shape : tuple  
Main dimension of the signal that specifies how many structured samples should be included. Structured scalar values have a shape of ().

dtype : numpy.dtype  
Structured NumPy dtype describing the whole structure.

values : list  
Optional. Values with which the signal is to be initialized. The values must be passed analog to the dtype of nested arrays - for two attributes e.g. a list with two arrays.

Example usage:

    structuredDtype = numpy.dtype([
        ('StructA', [
            ('SubStructA', [
                ('SubArrayA', int, (4,)),
                ('SubScalarA', int)])],
         (3,))
    ])
    s = StructuredSignal(shape=(5,), dtype=structuredDtype)

A [`StructuredSignal`](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignal "tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignal (Python class) — Creates a StructuredSignal if dtype is structured or a StructuredSignalLeaf if dtype is not structured ("flat").") can contain any number of [`StructuredSignalLeaf`](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf "tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf (Python class) — Represents a leaf element of a StructuredSignal. Should not be created directly, but by creating a StructuredSignal with a dtype representing a "flat structure".") or further nested [`StructuredSignal`](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignal "tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignal (Python class) — Creates a StructuredSignal if dtype is structured or a StructuredSignalLeaf if dtype is not structured ("flat")."). In the example the [`StructuredSignalLeaf`](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf "tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf (Python class) — Represents a leaf element of a StructuredSignal. Should not be created directly, but by creating a StructuredSignal with a dtype representing a "flat structure".") `s.SubStructA.SubArrayA` contains an array of shape (5, 3, 4).

An example for valid initial values looks like this:

    values=[[[
        numpy.arange(5 * 3 * 4).reshape((5, 3, 4)),  # SubArrayA
        numpy.arange(5 * 3).reshape((5, 3)),         # SubScalarA
    ]]]

The depth is the same as in the dtype definition. (Tip: Count the number of opening square brackets up to the concerning leaf in the dtype definition.)

Alternatively, a [`StructuredSignal`](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignal "tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignal (Python class) — Creates a StructuredSignal if dtype is structured or a StructuredSignalLeaf if dtype is not structured ("flat").") can be constructed empty and inititialized later on:

    s[0].StructA[0].SubStructA.SubScalarA = 12
    s[1].StructA.SubStructA.SubArrayA[1] = 2             # initializes all elements of StructA
    s[2].StructA[1].SubStructA.SubArrayA = [1, 2, 3, 4]
    s[2].StructA[2].SubStructA.SubArrayA = [1, 2, 3]     # SubArray[3:5] remains empty (masked)

GetName()[¶](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignal.GetName "Link to this definition")  
Returns the name of the structured element. (Is None for the top level structure.)

GetElementNames()[¶](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignal.GetElementNames "Link to this definition")  
Returns a list containing the names of the direct child elements.

IterElements()[¶](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignal.IterElements "Link to this definition")  
Iterates over the direct child elements by returning a tuple of the name and the element itself.

## StructuredSignalLeaf[¶](#structuredsignalleaf "Link to this heading")

*class* StructuredSignalLeaf[¶](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf "Link to this definition")  
Represents a leaf element of a [`StructuredSignal`](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignal "tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignal (Python class) — Creates a StructuredSignal if dtype is structured or a StructuredSignalLeaf if dtype is not structured ("flat")."). Should not be created directly, but by creating a [`StructuredSignal`](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignal "tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignal (Python class) — Creates a StructuredSignal if dtype is structured or a StructuredSignalLeaf if dtype is not structured ("flat").") with a dtype representing a “flat structure”.

See [`StructuredSignal`](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignal "tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignal (Python class) — Creates a StructuredSignal if dtype is structured or a StructuredSignalLeaf if dtype is not structured ("flat").") for an example.

Working with raw values: Raw values can be added and accessed using the \_raw attribute. Valid node values take precedence over raw values during processing. If node values are masked, e.g. because of a failed conversion, raw values are used if present.

min(*\*[args](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.min "tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.min.args (Python parameter)")*, *\*\*[kwargs](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.min "tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.min.kwargs (Python parameter)")*)[¶](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.min "Link to this definition")  
Return the minimum.

Return type:  int|float

max(*\*[args](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.max "tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.max.args (Python parameter)")*, *\*\*[kwargs](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.max "tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.max.kwargs (Python parameter)")*)[¶](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.max "Link to this definition")  
Return the maximum.

Return type:  int|float

any(*\*[args](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.any "tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.any.args (Python parameter)")*, *\*\*[kwargs](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.any "tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.any.kwargs (Python parameter)")*)[¶](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.any "Link to this definition")  
Returns True if any of the elements evaluate to True.

Return type:  bool

all(*\*[args](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.all "tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.all.args (Python parameter)")*, *\*\*[kwargs](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.all "tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.all.kwargs (Python parameter)")*)[¶](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.all "Link to this definition")  
Returns True if all of the elements evaluate to True.

Return type:  bool

FullArray()[¶](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.FullArray "Link to this definition")  
Returns the full array represented by this leaf element, which allows regular indexing considering all dimensions.

By default, indexing a leaf element only considers the dimensions of the leaf element itself, not the dimensions originating from parent structure elements.

Example:

    structuredDtype = numpy.dtype([
        ('StructA', [('SubArrayA', int, (3,)),])
    ])
    s = StructuredSignal(shape=(2,), dtype=structuredDtype,
                         values=[[numpy.array([[1, 2, 3], [4, 5, 6]])]])
    leaf = s.StructA.SubArrayA
    # even though the shape of leaf is (2, 3), leaf[0] indexes SubArrayA
    # returning the first element of each of the 2 SubArrayA in StructA
    assert all(leaf[0] == numpy.array([1, 4]))
    assert len(leaf[0]) == 2
    # leaf.FullArray() returns a regular array of the shape (2, 3),
    # thus leaf[0] returns the whole first SubArrayA
    assert all(leaf.FullArray()[0] == numpy.array([1, 2, 3]))
    assert len(leaf.FullArray()[0]) == 3

GetName()[¶](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.GetName "Link to this definition")  
Returns the name of the structured element. (Is None for the top level structure.)

GetElementNames()[¶](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.GetElementNames "Link to this definition")  
Returns a list containing the names of the direct child elements.

Since [`StructuredSignalLeaf`](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf "tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf (Python class) — Represents a leaf element of a StructuredSignal. Should not be created directly, but by creating a StructuredSignal with a dtype representing a "flat structure".") is the final node there are no direct child elements and so this method just returns an empty list.

IterElements()[¶](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.IterElements "Link to this definition")  
Returns an empty iterator.

See [`StructuredSignalLeaf.GetElementNames()`](#tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.GetElementNames "tts.lib.dataStructures.structuredSignal.StructuredSignal.StructuredSignalLeaf.GetElementNames (Python method) — Returns a list containing the names of the direct child elements.").

## Inbox[¶](#inbox "Link to this heading")

*class* Inbox[¶](#tts.core.package.dataStructures.Inbox.Inbox "Link to this definition")  
IsEmpty()[¶](#tts.core.package.dataStructures.Inbox.Inbox.IsEmpty "Link to this definition")  
Checks if inbox is empty.

Returns:  True if inbox is empty else False

Return type:  boolean

GetCount()[¶](#tts.core.package.dataStructures.Inbox.Inbox.GetCount "Link to this definition")  
Returns the number of messages in the inbox.

Returns:  number of messages

Return type:  int

FetchNext(*[timeout](#tts.core.package.dataStructures.Inbox.Inbox.FetchNext.timeout "tts.core.package.dataStructures.Inbox.Inbox.FetchNext.timeout (Python parameter) — timeout in milliseconds to wait for the next message income. If None the standard timeout is used. The Value -1 defines no timeout equal to infinte waiting.")=`None`*)[¶](#tts.core.package.dataStructures.Inbox.Inbox.FetchNext "Link to this definition")  
Fetches the next message in the inbox.

Parameters:  timeout : int[¶](#tts.core.package.dataStructures.Inbox.Inbox.FetchNext.timeout "Permalink to this definition")  
timeout in milliseconds to wait for the next message income. If None the standard timeout is used. The Value -1 defines no timeout equal to infinte waiting.

Returns:  next message

Return type:  object

LookUpNext(*[timeout](#tts.core.package.dataStructures.Inbox.Inbox.LookUpNext.timeout "tts.core.package.dataStructures.Inbox.Inbox.LookUpNext.timeout (Python parameter) — timeout in milliseconds to wait for the next message income. If None the standard timeout is used. The Value -1 defines no timeout equal to infinte waiting.")=`None`*)[¶](#tts.core.package.dataStructures.Inbox.Inbox.LookUpNext "Link to this definition")  
Looks for next message in inbox without fetching it.

Parameters:  timeout : int[¶](#tts.core.package.dataStructures.Inbox.Inbox.LookUpNext.timeout "Permalink to this definition")  
timeout in milliseconds to wait for the next message income. If None the standard timeout is used. The Value -1 defines no timeout equal to infinte waiting.

Returns:  message name

Return type:  string

## Outbox[¶](#outbox "Link to this heading")

*class* Outbox[¶](#tts.core.package.dataStructures.Outbox.Outbox "Link to this definition")  
Post(*[value](#tts.core.package.dataStructures.Outbox.Outbox.Post.value "tts.core.package.dataStructures.Outbox.Outbox.Post.value (Python parameter) — message")*)[¶](#tts.core.package.dataStructures.Outbox.Outbox.Post "Link to this definition")  
Sends a message to the connected outbox.

Parameters:  value : object[¶](#tts.core.package.dataStructures.Outbox.Outbox.Post.value "Permalink to this definition")  
message

IsConnected()[¶](#tts.core.package.dataStructures.Outbox.Outbox.IsConnected "Link to this definition")  
Checks if outbox is connected to a target.

Returns:  True if outbox is connected, else None.

Return type:  boolean

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEzIDIwaC0yVjhsLTUuNSA1LjUtMS40Mi0xLjQyTDEyIDQuMTZsNy45MiA3LjkyLTEuNDIgMS40MkwxMyA4eiIgLz48L3N2Zz4=) Back to top
