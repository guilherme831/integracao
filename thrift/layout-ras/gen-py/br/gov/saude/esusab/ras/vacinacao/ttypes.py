#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
import br.gov.saude.esusab.ras.common.ttypes


from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class VacinaRowThrift:
  """
  Attributes:
   - imunobiologico
   - estrategiaVacinacao
   - dose
   - lote
   - fabricante
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'imunobiologico', None, None, ), # 1
    (2, TType.I64, 'estrategiaVacinacao', None, None, ), # 2
    (3, TType.I64, 'dose', None, None, ), # 3
    (4, TType.STRING, 'lote', None, None, ), # 4
    (5, TType.STRING, 'fabricante', None, None, ), # 5
  )

  def __init__(self, imunobiologico=None, estrategiaVacinacao=None, dose=None, lote=None, fabricante=None,):
    self.imunobiologico = imunobiologico
    self.estrategiaVacinacao = estrategiaVacinacao
    self.dose = dose
    self.lote = lote
    self.fabricante = fabricante

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.imunobiologico = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.estrategiaVacinacao = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.dose = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.lote = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.fabricante = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('VacinaRowThrift')
    if self.imunobiologico is not None:
      oprot.writeFieldBegin('imunobiologico', TType.I64, 1)
      oprot.writeI64(self.imunobiologico)
      oprot.writeFieldEnd()
    if self.estrategiaVacinacao is not None:
      oprot.writeFieldBegin('estrategiaVacinacao', TType.I64, 2)
      oprot.writeI64(self.estrategiaVacinacao)
      oprot.writeFieldEnd()
    if self.dose is not None:
      oprot.writeFieldBegin('dose', TType.I64, 3)
      oprot.writeI64(self.dose)
      oprot.writeFieldEnd()
    if self.lote is not None:
      oprot.writeFieldBegin('lote', TType.STRING, 4)
      oprot.writeString(self.lote)
      oprot.writeFieldEnd()
    if self.fabricante is not None:
      oprot.writeFieldBegin('fabricante', TType.STRING, 5)
      oprot.writeString(self.fabricante)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.imunobiologico)
    value = (value * 31) ^ hash(self.estrategiaVacinacao)
    value = (value * 31) ^ hash(self.dose)
    value = (value * 31) ^ hash(self.lote)
    value = (value * 31) ^ hash(self.fabricante)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class FichaVacinacaoChildThrift:
  """
  Attributes:
   - turno
   - numProntuario
   - cnsCidadao
   - dtNascimento
   - sexo
   - localAtendimento
   - viajante
   - comunicanteHanseniase
   - gestante
   - puerpera
   - vacinas
  """

  thrift_spec = (
    None, # 0
    (1, TType.I64, 'turno', None, None, ), # 1
    (2, TType.STRING, 'numProntuario', None, None, ), # 2
    (3, TType.STRING, 'cnsCidadao', None, None, ), # 3
    (4, TType.I64, 'dtNascimento', None, None, ), # 4
    (5, TType.I64, 'sexo', None, None, ), # 5
    (6, TType.I64, 'localAtendimento', None, None, ), # 6
    (7, TType.BOOL, 'viajante', None, None, ), # 7
    (8, TType.BOOL, 'comunicanteHanseniase', None, None, ), # 8
    (9, TType.BOOL, 'gestante', None, None, ), # 9
    (10, TType.BOOL, 'puerpera', None, None, ), # 10
    (11, TType.LIST, 'vacinas', (TType.STRUCT,(VacinaRowThrift, VacinaRowThrift.thrift_spec)), None, ), # 11
  )

  def __init__(self, turno=None, numProntuario=None, cnsCidadao=None, dtNascimento=None, sexo=None, localAtendimento=None, viajante=None, comunicanteHanseniase=None, gestante=None, puerpera=None, vacinas=None,):
    self.turno = turno
    self.numProntuario = numProntuario
    self.cnsCidadao = cnsCidadao
    self.dtNascimento = dtNascimento
    self.sexo = sexo
    self.localAtendimento = localAtendimento
    self.viajante = viajante
    self.comunicanteHanseniase = comunicanteHanseniase
    self.gestante = gestante
    self.puerpera = puerpera
    self.vacinas = vacinas

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I64:
          self.turno = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.numProntuario = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.cnsCidadao = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I64:
          self.dtNascimento = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I64:
          self.sexo = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.I64:
          self.localAtendimento = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.BOOL:
          self.viajante = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.BOOL:
          self.comunicanteHanseniase = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.BOOL:
          self.gestante = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.BOOL:
          self.puerpera = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.LIST:
          self.vacinas = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = VacinaRowThrift()
            _elem5.read(iprot)
            self.vacinas.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('FichaVacinacaoChildThrift')
    if self.turno is not None:
      oprot.writeFieldBegin('turno', TType.I64, 1)
      oprot.writeI64(self.turno)
      oprot.writeFieldEnd()
    if self.numProntuario is not None:
      oprot.writeFieldBegin('numProntuario', TType.STRING, 2)
      oprot.writeString(self.numProntuario)
      oprot.writeFieldEnd()
    if self.cnsCidadao is not None:
      oprot.writeFieldBegin('cnsCidadao', TType.STRING, 3)
      oprot.writeString(self.cnsCidadao)
      oprot.writeFieldEnd()
    if self.dtNascimento is not None:
      oprot.writeFieldBegin('dtNascimento', TType.I64, 4)
      oprot.writeI64(self.dtNascimento)
      oprot.writeFieldEnd()
    if self.sexo is not None:
      oprot.writeFieldBegin('sexo', TType.I64, 5)
      oprot.writeI64(self.sexo)
      oprot.writeFieldEnd()
    if self.localAtendimento is not None:
      oprot.writeFieldBegin('localAtendimento', TType.I64, 6)
      oprot.writeI64(self.localAtendimento)
      oprot.writeFieldEnd()
    if self.viajante is not None:
      oprot.writeFieldBegin('viajante', TType.BOOL, 7)
      oprot.writeBool(self.viajante)
      oprot.writeFieldEnd()
    if self.comunicanteHanseniase is not None:
      oprot.writeFieldBegin('comunicanteHanseniase', TType.BOOL, 8)
      oprot.writeBool(self.comunicanteHanseniase)
      oprot.writeFieldEnd()
    if self.gestante is not None:
      oprot.writeFieldBegin('gestante', TType.BOOL, 9)
      oprot.writeBool(self.gestante)
      oprot.writeFieldEnd()
    if self.puerpera is not None:
      oprot.writeFieldBegin('puerpera', TType.BOOL, 10)
      oprot.writeBool(self.puerpera)
      oprot.writeFieldEnd()
    if self.vacinas is not None:
      oprot.writeFieldBegin('vacinas', TType.LIST, 11)
      oprot.writeListBegin(TType.STRUCT, len(self.vacinas))
      for iter6 in self.vacinas:
        iter6.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.turno)
    value = (value * 31) ^ hash(self.numProntuario)
    value = (value * 31) ^ hash(self.cnsCidadao)
    value = (value * 31) ^ hash(self.dtNascimento)
    value = (value * 31) ^ hash(self.sexo)
    value = (value * 31) ^ hash(self.localAtendimento)
    value = (value * 31) ^ hash(self.viajante)
    value = (value * 31) ^ hash(self.comunicanteHanseniase)
    value = (value * 31) ^ hash(self.gestante)
    value = (value * 31) ^ hash(self.puerpera)
    value = (value * 31) ^ hash(self.vacinas)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class FichaVacinacaoMasterThrift:
  """
  Attributes:
   - uuidFicha
   - tpCdsOrigem
   - headerTransport
   - vacinacoes
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'uuidFicha', None, None, ), # 1
    (2, TType.I32, 'tpCdsOrigem', None, None, ), # 2
    (3, TType.STRUCT, 'headerTransport', (br.gov.saude.esusab.ras.common.ttypes.UnicaLotacaoHeaderThrift, br.gov.saude.esusab.ras.common.ttypes.UnicaLotacaoHeaderThrift.thrift_spec), None, ), # 3
    (4, TType.LIST, 'vacinacoes', (TType.STRUCT,(FichaVacinacaoChildThrift, FichaVacinacaoChildThrift.thrift_spec)), None, ), # 4
  )

  def __init__(self, uuidFicha=None, tpCdsOrigem=None, headerTransport=None, vacinacoes=None,):
    self.uuidFicha = uuidFicha
    self.tpCdsOrigem = tpCdsOrigem
    self.headerTransport = headerTransport
    self.vacinacoes = vacinacoes

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.uuidFicha = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.tpCdsOrigem = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRUCT:
          self.headerTransport = br.gov.saude.esusab.ras.common.ttypes.UnicaLotacaoHeaderThrift()
          self.headerTransport.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.LIST:
          self.vacinacoes = []
          (_etype10, _size7) = iprot.readListBegin()
          for _i11 in xrange(_size7):
            _elem12 = FichaVacinacaoChildThrift()
            _elem12.read(iprot)
            self.vacinacoes.append(_elem12)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('FichaVacinacaoMasterThrift')
    if self.uuidFicha is not None:
      oprot.writeFieldBegin('uuidFicha', TType.STRING, 1)
      oprot.writeString(self.uuidFicha)
      oprot.writeFieldEnd()
    if self.tpCdsOrigem is not None:
      oprot.writeFieldBegin('tpCdsOrigem', TType.I32, 2)
      oprot.writeI32(self.tpCdsOrigem)
      oprot.writeFieldEnd()
    if self.headerTransport is not None:
      oprot.writeFieldBegin('headerTransport', TType.STRUCT, 3)
      self.headerTransport.write(oprot)
      oprot.writeFieldEnd()
    if self.vacinacoes is not None:
      oprot.writeFieldBegin('vacinacoes', TType.LIST, 4)
      oprot.writeListBegin(TType.STRUCT, len(self.vacinacoes))
      for iter13 in self.vacinacoes:
        iter13.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.uuidFicha is None:
      raise TProtocol.TProtocolException(message='Required field uuidFicha is unset!')
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.uuidFicha)
    value = (value * 31) ^ hash(self.tpCdsOrigem)
    value = (value * 31) ^ hash(self.headerTransport)
    value = (value * 31) ^ hash(self.vacinacoes)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
