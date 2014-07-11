__author__ = 'Apollo117'
# wrapper.py, a weak wrapper for libspice.py, here is where all the important ctypes setup and returning occurs.


import ctypes
import SpiceyPy.SupportTypes as stypes
from SpiceyPy.libspice import libspice
import numpy

########################################################################################################################
# A


def appndc(item, cell):
    assert isinstance(cell, stypes.SpiceCell)
    item = stypes.strtocharpoint(item)
    libspice.appndc_c(item, cell)
    pass


def appndd(item, cell):
    #Todo: Test appndd
    assert isinstance(cell, stypes.SpiceCell)
    item = ctypes.c_double(item)
    libspice.appndd_c(item, cell)
    pass


def appndi(item, cell):
    #Todo: Test appndi
    assert isinstance(cell, stypes.SpiceCell)
    item = ctypes.c_int(item)
    libspice.appndi_c(item, cell)
    pass


def axisar(axis, angle):
    #todo: test axisar
    axis = stypes.toDoubleVector(axis)
    angle = ctypes.c_double(angle)
    r = stypes.doubleMatrix()
    libspice.axisar_c(axis, angle, r)
    return stypes.matrixToList(r)

########################################################################################################################
# B


def b1900():
    return libspice.b1900_c()


def b1950():
    return libspice.b1950_c()


def badkpv(caller, name, comp, insize, divby, intype):
    #todo: test badkpv
    caller = stypes.strtocharpoint(caller)
    name = stypes.strtocharpoint(name)
    comp = stypes.strtocharpoint(comp)
    insize = ctypes.c_int(insize)
    divby = ctypes.c_int(divby)
    intype = stypes.strtocharpoint(intype)
    return libspice.badkpv(caller, name, comp, insize, divby, intype)


def bodc2n(code, lenout):
    #todo: test bodc2n
    code = ctypes.c_int(code)
    name = stypes.strtocharpoint(" "*lenout)
    lenout = ctypes.c_int(lenout)
    found = ctypes.c_bool(0)
    libspice.bodc2n_c(code, lenout, name, ctypes.byref(found))
    return name.value


def bodc2s(code, lenout):
    #todo: test bodc2s
    code = ctypes.c_int(code)
    name = stypes.strtocharpoint(" "*lenout)
    lenout = ctypes.c_int(lenout)
    libspice.bodc2s_c(code, lenout, name)
    return name.value


def boddef(name, code):
    #todo: test boddef
    name = stypes.strtocharpoint(name)
    code = ctypes.c_int(code)
    libspice.boddef_c(name, code)
    pass


def bodfnd(body, item):
    body = ctypes.c_int(body)
    item = stypes.strtocharpoint(item)
    return libspice.bodfnd(body, item)


def bodn2c(name):
    name = stypes.strtocharpoint(name)
    code = ctypes.c_int(0)
    found = ctypes.c_bool(0)
    libspice.bodn2c_c(name, ctypes.byref(code), ctypes.byref(found))
    if found.value:
        return code.value
    else:
        return None


def bods2c(name):
    #Todo: test bods2c
    name = stypes.strtocharpoint(name)
    code = ctypes.c_int(0)
    found = ctypes.c_bool(0)
    libspice.bods2c_c(name, ctypes.byref(code), ctypes.byref(found))
    if found.value:
        return code.value
    else:
        return None


def bodvar(body, item, dim):
    #Todo: test bodvar
    body = ctypes.c_int(body)
    dim = ctypes.c_int(dim)
    item = stypes.strtocharpoint(item)
    values = stypes.doubleVector(dim.value)
    libspice.bodvar(body, item, ctypes.byref(dim), values)
    return stypes.vectorToList(values)


def bodvcd(bodyid, item, maxn):
    #todo: test bodvcd
    bodyid = ctypes.c_int(bodyid)
    item = stypes.strtocharpoint(item)
    maxn = ctypes.c_int(maxn)
    dim = ctypes.c_int(0)
    values = stypes.doubleVector(maxn)
    libspice.bodvcd_c(bodyid, item, maxn, ctypes.byref(dim), values)
    return stypes.vectorToList(values)


def bodvrd(bodynm, item, maxn):
    bodynm = stypes.strtocharpoint(bodynm)
    item = stypes.strtocharpoint(item)
    maxn = ctypes.c_int(maxn)
    dim = ctypes.c_int(0)
    values = stypes.doubleVector(3)
    libspice.bodvrd_c(bodynm, item, maxn, ctypes.byref(dim), values)
    return stypes.vectorToList(values)


def brcktd(number, end1, end2):
    number = ctypes.c_double(number)
    end1 = ctypes.c_double(end1)
    end2 = ctypes.c_double(end2)
    return libspice.brcktd_c(number, end1, end2)


def brckti(number, end1, end2):
    number = ctypes.c_int(number)
    end1 = ctypes.c_int(end1)
    end2 = ctypes.c_int(end2)
    return libspice.brckti_c(number, end1, end2)


def bschoc(value, ndim, lenvals, array, order):
    #todo: Fix, probably not working
    value = stypes.strtocharpoint(value)
    ndim = ctypes.c_int(ndim)
    lenvals = ctypes.c_int(lenvals)
    array = stypes.listtocharvector(array)
    order = stypes.toIntVector(order)
    return libspice.bschoc(value, ndim, lenvals, ctypes.byref(array), ctypes.byref(order))


def bschoi(value, ndim, array, order):
    #todo: Fix, this is not working
    value = ctypes.c_int(value)
    ndim = ctypes.c_int(ndim)
    order = stypes.toIntVector(order)
    array = stypes.toIntVector(array)
    return libspice.bschoi_c(value, ndim, ctypes.byref(order), ctypes.byref(array))


def bsrchc(value, ndim, lenvals, array):
    value = stypes.strtocharpoint(value)
    ndim = ctypes.c_int(ndim)
    lenvals = ctypes.c_int(lenvals)
    array = stypes.listToCharArrayPtr(array, xLen=lenvals, yLen=ndim)
    return libspice.bsrchc_c(value, ndim, lenvals, array)


def bsrchd(value, ndim, array):
    value = ctypes.c_double(value)
    ndim = ctypes.c_int(ndim)
    array = stypes.toDoubleVector(array)
    return libspice.bsrchd_c(value, ndim, array)


def bsrchi(value, ndim, array):
    value = ctypes.c_int(value)
    ndim = ctypes.c_int(ndim)
    array = stypes.toIntVector(array)
    return libspice.bsrchi_c(value, ndim, array)


########################################################################################################################
# C


def card(cell):
    #Todo: Test card
    return libspice.card_c(ctypes.byref(cell))


def cgv2el(center, vec1, vec2):
    #Todo: test cgv2el
    center = stypes.toDoubleVector(center)
    vec1 = stypes.toDoubleVector(vec1)
    vec2 = stypes.toDoubleVector(vec2)
    ellipse = stypes.Ellipse()
    libspice.cgv2el_c(center, vec1, vec2, ctypes.byref(ellipse))
    return ellipse


def chkin(module):
    #Todo: test chkin
    module = stypes.strtocharpoint(module)
    libspice.chkin_c(module)
    pass


def chkout(module):
    #Todo: test chkout
    module = stypes.strtocharpoint(module)
    libspice.chkout_c(module)
    pass


def cidfrm(cent, lenout):
    #Todo: test cidfrm
    cent = ctypes.c_int(cent)
    lenout = ctypes.c_int(lenout)
    frcode = ctypes.c_int()
    frname = stypes.strtocharpoint(lenout)
    found = ctypes.c_bool()
    libspice.cidfrm_c(cent, lenout, ctypes.byref(frcode), frname, ctypes.byref(found))
    return frcode.value, frname.value, found.value


def ckcls(handle):
    #Todo: test ckcls
    handle = ctypes.c_int(handle)
    libspice.ckcls_c(handle)
    pass


def ckcov(ck, idcode, needav, level, tol, timsys, cover=None):
    #Todo: test ckcov
    ck = stypes.strtocharpoint(ck)
    idcode = ctypes.c_int(idcode)
    needav = ctypes.c_bool(needav)
    level = stypes.strtocharpoint(level)
    tol = ctypes.c_double(tol)
    timsys = stypes.strtocharpoint(timsys)
    if not cover:
        cover = stypes.SPICEDOUBLE_CELL(2000)
    assert isinstance(cover, stypes.SpiceCell)
    assert cover.dtype == 1
    libspice.ckcov_c(ck, idcode, needav, level, tol, timsys, ctypes.byref(cover))
    return cover


def ckgp(inst, sclkdp, tol, ref):
    #Todo: test ckgp
    inst = ctypes.c_int(inst)
    sclkdp = ctypes.c_double(sclkdp)
    tol = ctypes.c_double(tol)
    ref = stypes.strtocharpoint(ref)
    cmat = stypes.doubleMatrix()
    clkout = ctypes.c_double()
    found = ctypes.c_bool()
    libspice.ckgp_c(inst, sclkdp, tol, ref, cmat, ctypes.byref(clkout), ctypes.byref(found))
    return stypes.matrixToList(cmat), clkout.value, found.value


def ckgpav(inst, sclkdp, tol, ref):
    #Todo: test ckgpav
    inst = ctypes.c_int(inst)
    sclkdp = ctypes.c_double(sclkdp)
    tol = ctypes.c_double(tol)
    ref = stypes.strtocharpoint(ref)
    cmat = stypes.doubleMatrix()
    av = stypes.doubleVector(3)
    clkout = ctypes.c_double()
    found = ctypes.c_bool()
    libspice.ckgpav_c(inst, sclkdp, tol, ref, cmat, av, ctypes.byref(clkout), ctypes.byref(found))
    return stypes.matrixToList(cmat), stypes.vectorToList(av), clkout.value, found.value


def cklpf(filename):
    #Todo: test cklpf
    filename = stypes.strtocharpoint(filename)
    handle = ctypes.c_int()
    libspice.cklpf_c(filename, ctypes.byref(handle))
    return handle.value


def ckobj(ck, ids):
    #Todo: test ckobj
    assert isinstance(ck, str)
    ck = stypes.strtocharpoint(ck)
    if not ids:
        ids = stypes.SPICEINT_CELL(1000)
    assert isinstance(ids, stypes.SpiceCell)
    assert ids.dtype == 2
    libspice.ckobj_c(ck, ctypes.byref(ids))
    return ids


def ckopn(filename, ifname, ncomch):
    #Todo: test ckopn
    filename = stypes.strtocharpoint(filename)
    ifname = stypes.strtocharpoint(ifname)
    ncomch = ctypes.c_int(ncomch)
    handle = ctypes.c_int()
    libspice.ckopn_c(filename, ifname, ncomch, ctypes.byref(handle))
    return handle.value


def ckupf(handle):
    #Todo: test ckupf
    handle = ctypes.c_int(handle)
    libspice.ckupf_c(handle)
    pass


def ckw01(handle, begtim, endtim, inst, ref, avflag, segid, nrec, sclkdp, quats, avvs):
    #Todo: test ckw01
    handle = ctypes.c_int(handle)
    begtim = ctypes.c_double(begtim)
    endtim = ctypes.c_double(endtim)
    inst = ctypes.c_int(inst)
    ref = stypes.strtocharpoint(ref)
    avflag = ctypes.c_bool(avflag)
    segid = stypes.strtocharpoint(segid)
    sclkdp = stypes.toDoubleVector(sclkdp)
    quats = stypes.listtodoublematrix(quats, x=4, y=nrec)  # may need to swap x and y values here
    avvs = stypes.listtodoublematrix(avvs, x=3, y=nrec)  # may need to swap x and y values here
    nrec = ctypes.c_int(nrec)  # looks like this defines the dimensions for quats and avvs
    libspice.ckw01_c(handle, begtim, endtim, inst, ref, avflag, segid, nrec,
                     ctypes.byref(sclkdp), ctypes.byref(quats), ctypes.byref(avvs))
    pass


def ckw02(handle, begtim, endtim, inst, ref, segid, nrec, start, stop, quats, avvs, rates):
    #Todo: test ckw02
    handle = ctypes.c_int(handle)
    begtim = ctypes.c_double(begtim)
    endtim = ctypes.c_double(endtim)
    inst = ctypes.c_int(inst)
    ref = stypes.strtocharpoint(ref)
    segid = stypes.strtocharpoint(segid)
    start = stypes.toDoubleVector(start)
    stop = stypes.toDoubleVector(stop)
    rates = stypes.toDoubleVector(rates)
    quats = stypes.listtodoublematrix(quats, x=4, y=nrec)  # may need to swap x and y values here
    avvs = stypes.listtodoublematrix(avvs, x=3, y=nrec)  # may need to swap x and y values here
    nrec = ctypes.c_int(nrec)  # looks like this defines the dimensions for quats and avvs
    libspice.ckw02_c(handle, begtim, endtim, inst, ref, segid, nrec, start, stop, quats, avvs, rates)
    pass


def ckw03(handle, begtim, endtim, inst, ref, avflag, segid, nrec, sclkdp, quats, avvs, nints, starts):
    #Todo: test ckw03
    handle = ctypes.c_int(handle)
    begtim = ctypes.c_double(begtim)
    endtim = ctypes.c_double(endtim)
    inst = ctypes.c_int(inst)
    ref = stypes.strtocharpoint(ref)
    avflag = ctypes.c_bool(avflag)
    segid = stypes.strtocharpoint(segid)
    sclkdp = stypes.toDoubleVector(sclkdp)
    quats = stypes.listtodoublematrix(quats, x=4, y=nrec)  # may need to swap x and y values here
    avvs = stypes.listtodoublematrix(avvs, x=3, y=nrec)  # may need to swap x and y values here
    nrec = ctypes.c_int(nrec)  # looks like this defines the dimensions for quats and avvs
    starts = stypes.toDoubleVector(starts)
    nints = ctypes.c_int(nints)
    libspice.ckw03_c(handle, begtim, endtim, inst, ref, avflag, segid, nrec,
                     ctypes.byref(sclkdp), ctypes.byref(quats), ctypes.byref(avvs), nints, ctypes.byref(starts))
    pass


# ckw05, skipping, ck05subtype?


def clight():
    #Todo: test clight
    return libspice.clight_c()


def clpool():
    #Todo: test clpool
    libspice.clpool_c()
    pass


def cmprss(delim, n, instr, lenout):
    #Todo: test cmprss
    delim = ctypes.c_char(delim)  # may have to decode/encode...
    n = ctypes.c_int(n)
    instr = stypes.strtocharpoint(instr)
    lenout = ctypes.c_int(lenout)
    output = stypes.strtocharpoint(lenout)
    libspice.cmprss_c(delim, n, instr, lenout, output)
    return output.value


def cnmfrm(cname, lenout):
    #Todo: test cnmfrm
    lenout = ctypes.c_int(lenout)
    frname = stypes.strtocharpoint(lenout)
    cname = stypes.strtocharpoint(cname)
    found = ctypes.c_bool()
    frcode = ctypes.c_int()
    libspice.cnmfrm_c(cname, lenout, ctypes.byref(frcode), frname, ctypes.byref(found))
    return frcode.value, frname.value, found.value


def conics(elts, et):
    #Todo: test conics
    elts = stypes.toDoubleVector(elts)
    et = ctypes.c_double(et)
    state = stypes.doubleVector(6)
    libspice.conics_c(elts, et, state)
    return stypes.vectorToList(state)


def convrt(x, inunit, outunit):
    x = ctypes.c_double(x)
    inunit = stypes.strtocharpoint(inunit)
    outunit = stypes.strtocharpoint(outunit)
    y = ctypes.c_double()
    libspice.convrt_c(x, inunit, outunit, ctypes.byref(y))
    return y.value


def copy(cell):
    #Todo: test copy, possible necessitates changes to SpiceCell as new object has the name base and data pointers
    assert isinstance(cell, stypes.SpiceCell)
    newcopy = stypes.SpiceCell(dtype=cell.dtype, length=cell.length, size=cell.size, card=cell.card, isSet=cell.isSet, base=cell.base, data=cell.data)
    libspice.copy_c(ctypes.byref(cell), ctypes.byref(newcopy))
    return newcopy


def cpos(string, chars, start):
    #Todo: test cpos
    string = stypes.strtocharpoint(string)
    chars = stypes.strtocharpoint(chars)
    start = ctypes.c_int(start)
    return libspice.cpos_c(string, chars, start)


def cposr(string, chars, start):
    #Todo: test cposr
    string = stypes.strtocharpoint(string)
    chars = stypes.strtocharpoint(chars)
    start = ctypes.c_int(start)
    return libspice.cposr_c(string, chars, start)


def cvpool(agent):
    #Todo: test cvpool
    agent = stypes.strtocharpoint(agent)
    update = ctypes.c_bool()
    libspice.cvpool_c(agent, ctypes.byref(update))
    return update.value


def cyllat(r, lonc, z):
    #Todo: test cyllat
    r = ctypes.c_double(r)
    lonc = ctypes.c_double(lonc)
    z = ctypes.c_double(z)
    radius = ctypes.c_double()
    lon = ctypes.c_double()
    lat = ctypes.c_double()
    libspice.cyllat_c(r, lonc, z, ctypes.byref(radius), ctypes.byref(lon), ctypes.byref(lat))
    return radius.value, lon.value, lat.value


def cylrec(r, lon, z):
    #Todo: test cylrec
    r = ctypes.c_double(r)
    lon = ctypes.c_double(lon)
    z = ctypes.c_double(z)
    rectan = stypes.doubleVector(3)
    libspice.cylrec_c(r, lon, z, rectan)
    return stypes.vectorToList(rectan)


def cylsph(r, lonc, z):
    #Todo: test cylsph
    r = ctypes.c_double(r)
    lonc = ctypes.c_double(lonc)
    z = ctypes.c_double(z)
    radius = ctypes.c_double()
    colat = ctypes.c_double()
    lon = ctypes.c_double()
    libspice.cyllat_c(r, lonc, z, ctypes.byref(radius), ctypes.byref(colat), ctypes.byref(lon))
    return radius.value, colat.value, lon.value


########################################################################################################################
# D

def dafac(handle, n, lenvals, buffer):
    #Todo: test dafac
    handle = ctypes.c_int(handle)
    buffer = stypes.listToCharArrayPtr(buffer, xLen=lenvals, yLen=n)
    n = ctypes.c_int(n)
    lenvals = ctypes.c_int(lenvals)
    libspice.dafac_c(handle, n, lenvals, ctypes.byref(buffer))
    pass


def dafbbs(handle):
    #Todo: test dafbbs
    handle = ctypes.c_int(handle)
    libspice.dafbbs_c(handle)
    pass


def dafbfs(handle):
    #Todo: test dafbfs
    handle = ctypes.c_int(handle)
    libspice.dafbfs_c(handle)
    pass


def dafcls(handle):
    #Todo: test dafcls
    handle = ctypes.c_int(handle)
    libspice.dafcls_c(handle)
    pass


def dafcs(handle):
    #Todo: test dafcs
    handle = ctypes.c_int(handle)
    libspice.dafcs_c(handle)
    pass


def dafdc(handle):
    #Todo: test dafdc
    handle = ctypes.c_int(handle)
    libspice.dafcc_c(handle)
    pass


def dafec(handle, bufsiz, lenout):
    #Todo: test dafec
    handle = ctypes.c_int(handle)
    buffer = stypes.charvector(bufsiz, lenout)
    bufsiz = ctypes.c_int(bufsiz)
    lenout = ctypes.c_int(lenout)
    n = ctypes.c_int()
    done = ctypes.c_bool()
    libspice.dafec_c(handle, bufsiz, lenout, ctypes.byref(n), ctypes.byref(buffer), ctypes.byref(done))
    return n.value, stypes.vectorToList(buffer), done.value


def daffna():
    #Todo: test daffna
    found = ctypes.c_bool()
    libspice.daffna_c(ctypes.byref(found))
    return found.value


def daffpa():
    #Todo: todo daffpa
    found = ctypes.c_bool()
    libspice.daffpa_c(ctypes.byref(found))
    return found.value


def dafgda(handle, begin, end):
    #Todo: test dafgda , is it returning an array?
    handle = ctypes.c_int(handle)
    begin = ctypes.c_int(begin)
    end = ctypes.c_int(end)
    data = ctypes.c_double()
    libspice.dafgda_c(handle, begin, end, ctypes.byref(data))
    return data.value


def dafgn(lenout):
    #Todo: test dafgn
    lenout = ctypes.c_int(lenout)
    name = stypes.strtocharpoint(lenout)
    libspice.dafgn_c(lenout, name)
    return name.value


def dafgs():
    #todo test dafgs, is this a valid way of getting a double array back?
    retarray = ctypes.c_double()
    libspice.dafgs_c(ctypes.byref(retarray))
    return stypes.vectorToList(retarray)


def dafgsr(handle, recno, begin, end):
    #Todo test dafgsr
    handle = ctypes.c_int(handle)
    recno = ctypes.c_int(recno)
    begin = ctypes.c_int(begin)
    end = ctypes.c_int(end)
    data = ctypes.c_double()
    found = ctypes.c_bool()
    libspice.dafgsr_c(handle, recno, begin, end, ctypes.byref(data), ctypes.byref(found))
    return data.value, found.value


def dafopr(fname):
    #Todo: test dafopr
    fname = stypes.strtocharpoint(fname)
    handle = ctypes.c_int()
    libspice.dafopr_c(fname, ctypes.byref(handle))
    return handle.value


def dafopw(fname):
    #Todo: test dafopw
    fname = stypes.strtocharpoint(fname)
    handle = ctypes.c_int()
    libspice.dafopw_c(fname, ctypes.byref(handle))
    return handle.value


def dafps(nd, ni, dc, ic):
    #Todo: test dafps
    dc = stypes.toDoubleVector(dc)
    ic = stypes.toIntVector(ic)
    outsum = stypes.doubleVector(nd+ni)
    nd = ctypes.c_int(nd)
    ni = ctypes.c_int(ni)
    libspice.dafps_c(nd, ni, ctypes.byref(dc), ctypes.byref(ic), ctypes.byref(outsum))
    return stypes.vectorToList(outsum)


def dafrda(handle, begin, end):
    #Todo: test dafrda
    handle = ctypes.c_int(handle)
    begin = ctypes.c_int(begin)
    end = ctypes.c_int(end)
    data = stypes.doubleVector(8)  # value of 8 from help file
    libspice.dafrda_c(handle, begin, end, ctypes.byref(data))
    return stypes.vectorToList(data)


def dafrfr(handle, lenout):
    #Todo: test dafrfr
    handle = ctypes.c_int(handle)
    lenout = ctypes.c_int(lenout)
    nd = ctypes.c_int()
    ni = ctypes.c_int()
    ifname = stypes.strtocharpoint(lenout)
    fward = ctypes.c_int()
    bward = ctypes.c_int()
    free = ctypes.c_int()
    libspice.dafrfr_c(handle, lenout, ctypes.byref(nd), ctypes.byref(ni), ifname, ctypes.byref(fward), ctypes.byref(bward), ctypes.byref(free))
    return nd.value, ni.value, ifname.value, fward.value, bward.value, free.value


def dafrs(insum):
    #Todo: test dafrs
    insum = stypes.toDoubleVector(insum)
    libspice.dafrs_c(ctypes.byref(insum))
    pass


def dafus(insum, nd, ni):
    #Todo: test dafus
    insum = stypes.toDoubleVector(insum)
    dc = stypes.doubleVector(nd)
    ic = stypes.intVector(ni)
    nd = ctypes.c_int(nd)
    ni = ctypes.c_int(ni)
    libspice.dafus_c(insum, nd, ni, dc, ic)
    return stypes.vectorToList(dc), stypes.vectorToList(ic)


def dasac(handle, n, buflen, buffer):
    #Todo: test dasac
    handle = ctypes.c_int(handle)
    buffer = stypes.charvector(n, buflen)
    n = ctypes.c_int(n)
    buflen = ctypes.c_int(buflen)
    libspice.dasac_c(handle, n, buflen, ctypes.byref(buffer))
    return stypes.vectorToList(buffer)


def dascls(handle):
    #Todo: test dafdc
    handle = ctypes.c_int(handle)
    libspice.dascls_c(handle)
    pass


def dasec(handle, bufsiz, buflen):
    #Todo: test dasec
    handle = ctypes.c_int(handle)
    buffer = stypes.charvector(bufsiz, buflen)
    bufsiz = ctypes.c_int(bufsiz)
    buflen = ctypes.c_int(buflen)
    n = ctypes.c_int()
    done = ctypes.c_bool()
    libspice.dafec_c(handle, bufsiz, buflen, ctypes.byref(n), ctypes.byref(buffer), ctypes.byref(done))
    return n.value, stypes.vectorToList(buffer), done.value


def dasopr(fname):
    #Todo: test dasopr
    fname = stypes.strtocharpoint(fname)
    handle = ctypes.c_int()
    libspice.dasopr_c(fname, ctypes.byref(handle))


def dcyldr(x, y, z):
    #Todo: test dlatdr
    x = ctypes.c_double(x)
    y = ctypes.c_double(y)
    z = ctypes.c_double(z)
    jacobi = stypes.doubleMatrix()
    libspice.dcyldr_c(x, y, z, jacobi)


def deltet(epoch, eptype):
    #Todo: test deltet
    epoch = ctypes.c_double(epoch)
    eptype = stypes.strtocharpoint(eptype)
    delta = ctypes.c_double()
    libspice.deltet_c(epoch, eptype, ctypes.byref(delta))
    return delta.value


def det(m1):
    #Todo: test det
    m1 = stypes.listtodoublematrix(m1)
    return libspice.det_c(m1)


def dgeodr(x, y, z, re, f):
    #Todo: test dgeodr
    x = ctypes.c_double(x)
    y = ctypes.c_double(y)
    z = ctypes.c_double(z)
    re = ctypes.c_double(re)
    f = ctypes.c_double(f)
    jacobi = stypes.doubleMatrix()
    libspice.dgeodr_c(x, y, z, re, f, jacobi)
    return stypes.matrixToList(jacobi)


def diags2(symmat):
    #Todo: test diags2
    symmat = stypes.listtodoublematrix(symmat, x=2, y=2)
    diag = stypes.doubleMatrix(x=2, y=2)
    rotateout = stypes.doubleMatrix(x=2, y=2)
    libspice.diags2_c(symmat, diag, rotateout)
    return stypes.matrixToList(diag), stypes.matrixToList(rotateout)


def diff(a, b):
    #Todo: test diff, this cell handleing may work for copy.
    assert isinstance(a, stypes.SpiceCell)
    assert isinstance(b, stypes.SpiceCell)
    assert a.dtype == b.dtype
    assert a.dtype == 0 or a.dtype == 1 or a.dtype == 2
    if a.dtype is 0:
        c = stypes.SPICECHAR_CELL(a.size, a.length)
    if a.dtype is 1:
        c = stypes.SPICEDOUBLE_CELL(a.size)
    elif a.dtype is 2:
        c = stypes.SPICEINT_CELL(a.size)
    else:
        raise NotImplementedError
    libspice.diff_c(ctypes.byref(a), ctypes.byref(b), ctypes.byref(c))
    return c


def dlatdr(x, y, z):
    #Todo: test dlatdr
    x = ctypes.c_double(x)
    y = ctypes.c_double(y)
    z = ctypes.c_double(z)
    jacobi = stypes.doubleMatrix()
    libspice.dlatdr_c(x, y, z, jacobi)


def dp2hx(number, lenout):
    #Works, but interesting results, you must add 1 to lenout
    #for it to work properly, so string length may need to be
    #handled with some process that adds one to the length
    #or removes the user from making the decision entirely
    #may be what causes certin strings to fail
    number = ctypes.c_double(number)
    lenout = ctypes.c_int(lenout)
    string = stypes.strtocharpoint(lenout)
    length = ctypes.c_int()
    libspice.dp2hx_c(number, lenout, string, ctypes.byref(length))
    return string.value, length.value


def dpgrdr(body, x, y, z, re, f):
    #Todo: test dpgrdr
    body = stypes.strtocharpoint(body)
    x = ctypes.c_double(x)
    y = ctypes.c_double(y)
    z = ctypes.c_double(z)
    re = ctypes.c_double(re)
    f = ctypes.c_double(f)
    jacobi = stypes.doubleMatrix()
    libspice.dpgrdr_c(body, x, y, z, re, f, jacobi)
    return stypes.matrixToList(jacobi)


def dpmax():
    #Todo: test dpmax
    return libspice.dpmax_c()


def dpmin():
    #Todo: test dpmin
    return libspice.dpmin_c()


def dpr():
    return libspice.dpr_c()


def drdcyl(r, lon, z):
    #Todo: drdcyl
    r = ctypes.c_double(r)
    lon = ctypes.c_double(lon)
    z = ctypes.c_double(z)
    jacobi = stypes.doubleMatrix()
    libspice.drdcyl_c(r, lon, z, jacobi)
    return stypes.matrixToList(jacobi)


def drdgeo(lon, lat, alt, re, f):
    #Todo: test drdgeo
    lon = ctypes.c_double(lon)
    lat = ctypes.c_double(lat)
    alt = ctypes.c_double(alt)
    re = ctypes.c_double(re)
    f = ctypes.c_double(f)
    jacobi = stypes.doubleMatrix()
    libspice.drdgeo_c(lon, lat, alt, re, f, jacobi)
    return stypes.matrixToList(jacobi)


def drdlat(r, lon, lat):
    #Todo: test drdsph
    r = ctypes.c_double(r)
    lon = ctypes.c_double(lon)
    lat = ctypes.c_double(lat)
    jacobi = stypes.doubleMatrix()
    libspice.drdsph_c(r, lon, lat, jacobi)
    return stypes.matrixToList(jacobi)


def drdpgr(body, lon, lat, alt, re, f):
    #Todo: test drdpgr
    body = stypes.strtocharpoint(body)
    lon = ctypes.c_double(lon)
    lat = ctypes.c_double(lat)
    alt = ctypes.c_double(alt)
    re = ctypes.c_double(re)
    f = ctypes.c_double(f)
    jacobi = stypes.doubleMatrix()
    libspice.drdpgr_c(body, lon, lat, alt, re, f, jacobi)
    return stypes.matrixToList(jacobi)


def drdsph(r, colat, lon):
    #Todo: test drdsph
    r = ctypes.c_double(r)
    colat = ctypes.c_double(colat)
    lon = ctypes.c_double(lon)
    jacobi = stypes.doubleMatrix()
    libspice.drdsph_c(r, colat, lon, jacobi)
    return stypes.matrixToList(jacobi)


def dsphdr(x, y, z):
    #Todo: test dsphdr
    x = ctypes.c_double(x)
    y = ctypes.c_double(y)
    z = ctypes.c_double(z)
    jacobi = stypes.doubleMatrix()
    libspice.dsphdr_c(x, y, z, jacobi)
    return stypes.matrixToList(jacobi)


def dtpool(name):
    #Todo: test dtpool
    name = stypes.strtocharpoint(name)
    found = ctypes.c_bool()
    n = ctypes.c_int()
    typeout = ctypes.c_char()
    libspice.dtpool_c(name, ctypes.byref(found), ctypes.byref(n), ctypes.byref(typeout))
    return found.value, n.value, typeout.value


def ducrss(s1, s2):
    #Todo: test dvcrss
    assert len(s1) is 6 and len(s2) is 6
    s1 = stypes.toDoubleVector(s1)
    s2 = stypes.toDoubleVector(s2)
    sout = stypes.doubleVector(6)
    libspice.ducrss_c(s1, s2, sout)
    return stypes.vectorToList(sout)


def dvcrss(s1, s2):
    #Todo: test dvcrss
    assert len(s1) is 6 and len(s2) is 6
    s1 = stypes.toDoubleVector(s1)
    s2 = stypes.toDoubleVector(s2)
    sout = stypes.doubleVector(6)
    libspice.dvcrss_c(s1, s2, sout)
    return stypes.vectorToList(sout)


def dvdot(s1, s2):
    #Todo: test dvdot
    assert len(s1) is 6 and len(s2) is 6
    s1 = stypes.toDoubleVector(s1)
    s2 = stypes.toDoubleVector(s2)
    return libspice.dvdot_c(s1, s2)


def dvhat(s1):
    #Todo: test dvhat
    assert len(s1) is 6
    s1 = stypes.toDoubleVector(s1)
    sout = stypes.doubleVector(6)
    libspice.dvhat_c(s1, sout)
    return stypes.vectorToList(sout)


def dvnorm(state):
    #Todo: test dvnorm
    assert len(state) is 6
    state = stypes.toDoubleVector(state)
    return libspice.dvnorm_c(state)


def dvpool(name):
    #Todo: test dvpool
    name = stypes.strtocharpoint(name)
    libspice.dvpool_c(name)
    pass


def dvsep(s1, s2):
    #Todo: test dvsep
    assert len(s1) is 6 and len(s2) is 6
    s1 = stypes.toDoubleVector(s1)
    s2 = stypes.toDoubleVector(s2)
    return libspice.dvsep_c(s1, s2)

########################################################################################################################
# E


def edlimb(a, b, c, viewpt):
    #Todo: test edlimb
    limb = stypes.Ellipse()
    a = ctypes.c_double(a)
    b = ctypes.c_double(b)
    c = ctypes.c_double(c)
    viewpt = stypes.toDoubleVector(viewpt)
    libspice.edlimb_c(a, b, c, viewpt, ctypes.byref(limb))
    return limb


def ekacec(handle, segno, recno, column, nvals, vallen, cvals, isnull):
    #Todo: test ekacec
    handle = ctypes.c_int(handle)
    segno = ctypes.c_int(segno)
    recno = ctypes.c_int(recno)
    column = stypes.strtocharpoint(column)
    nvals = ctypes.c_int(nvals)
    vallen = ctypes.c_int(vallen)
    cvals = ctypes.cast(stypes.listtocharvector(cvals), ctypes.c_void_p())  #this may not work
    isnull = ctypes.c_bool(isnull)
    libspice.ekacec_c(handle, segno, recno, column, nvals, vallen, cvals, isnull)
    pass


def ekaced(handle, segno, recno, column, nvals, dvals, isnull):
    #Todo: test ekaced
    handle = ctypes.c_int(handle)
    segno = ctypes.c_int(segno)
    recno = ctypes.c_int(recno)
    column = stypes.strtocharpoint(column)
    nvals = ctypes.c_int(nvals)
    dvals = stypes.toDoubleVector(dvals)
    isnull = ctypes.c_bool(isnull)
    libspice.ekaced_c(handle, segno, recno, column, nvals, ctypes.byref(dvals), isnull)  # not sure
    pass


def ekacei(handle, segno, recno, column, nvals, ivals, isnull):
    #Todo: test ekacei
    handle = ctypes.c_int(handle)
    segno = ctypes.c_int(segno)
    recno = ctypes.c_int(recno)
    column = stypes.strtocharpoint(column)
    nvals = ctypes.c_int(nvals)
    ivals = stypes.toIntVector(ivals)
    isnull = ctypes.c_bool(isnull)
    libspice.ekacei_c(handle, segno, recno, column, nvals, ctypes.byref(ivals), isnull)  # not sure
    pass


def ekaclc(handle, segno, column, vallen, cvals, entszs, nlflgs, rcptrs, wkindx):
    #Todo: test ekaclc
    handle = ctypes.c_int(handle)
    segno = ctypes.c_int(segno)
    column = stypes.strtocharpoint(column)
    vallen = ctypes.c_int(vallen)
    cvals = ctypes.cast(stypes.listtocharvector(cvals), ctypes.c_void_p())  # this may not work
    entszs = stypes.toIntVector(entszs)
    nlflgs = ctypes.c_bool(nlflgs)
    rcptrs = ctypes.c_int(rcptrs)
    wkindx = ctypes.c_int(wkindx)
    libspice.ekaclc_c(handle, segno, column, vallen, ctypes.byref(cvals), ctypes.byref(entszs), ctypes.byref(nlflgs), ctypes.byref(rcptrs), ctypes.cast(wkindx, ctypes.POINTER(ctypes.c_int)))
    return wkindx.value


def ekacld(handle, segno, column, dvals, entszs, nlflgs, rcptrs, wkindx):
    #Todo: test ekacld
    handle = ctypes.c_int(handle)
    segno = ctypes.c_int(segno)
    column = stypes.strtocharpoint(column)
    dvals = stypes.toIntVector(dvals)
    entszs = stypes.toIntVector(entszs)
    nlflgs = ctypes.c_bool(nlflgs)
    rcptrs = ctypes.c_int(rcptrs)
    wkindx = ctypes.c_int(wkindx)
    libspice.ekacld_c(handle, segno, column, ctypes.byref(dvals), ctypes.byref(entszs), ctypes.byref(nlflgs),
                      ctypes.byref(rcptrs), ctypes.cast(wkindx, ctypes.POINTER(ctypes.c_int)))
    return wkindx.value


def ekacli(handle, segno, column, ivals, entszs, nlflgs, rcptrs, wkindx):
    #Todo: test ekacli
    handle = ctypes.c_int(handle)
    segno = ctypes.c_int(segno)
    column = stypes.strtocharpoint(column)
    ivals = stypes.toDoubleVector(ivals)
    entszs = stypes.toIntVector(entszs)
    nlflgs = ctypes.c_bool(nlflgs)
    rcptrs = ctypes.c_int(rcptrs)
    wkindx = ctypes.c_int(wkindx)
    libspice.ekacli_c(handle, segno, column, ctypes.byref(ivals), ctypes.byref(entszs), ctypes.byref(nlflgs),
                      ctypes.byref(rcptrs), ctypes.cast(wkindx, ctypes.POINTER(ctypes.c_int)))
    return wkindx.value


def ekappr(handle, segno):
    #Todo: test ekappr
    handle = ctypes.c_int(handle)
    segno = ctypes.c_int(segno)
    recno = ctypes.c_int()
    libspice.ekappr_c(handle, segno, ctypes.byref(recno))
    return recno.value


def ekbseg(handle, tabnam, ncols, cnmlen, cnames, declen, decls):
    #Todo: test ekbseg
    handle = ctypes.c_int(handle)
    tabnam = stypes.strtocharpoint(tabnam)
    ncols = ctypes.c_int(ncols)
    cnmlen = ctypes.c_int(cnmlen)
    cnames = stypes.listtocharvector(cnames)  # not sure if this works
    declen = ctypes.c_int(declen)
    decls = stypes.listtocharvector(decls)
    segno = ctypes.c_int()
    libspice.ekbseg_c(handle, tabnam, ncols, cnmlen, cnames, declen, decls, ctypes.byref(segno))
    return segno.value


def ekccnt(table):
    #Todo: test ekccnt
    table = stypes.listtocharvector(table)
    ccount = ctypes.c_int()
    libspice.ekccnt_c(table, ctypes.byref(ccount))
    return ccount.value


def ekcii(table, cindex, lenout):
    #Todo: test ekcii SpiceEKAttDsc data type
    table = stypes.strtocharpoint(table)
    cindex = ctypes.c_int(cindex)
    lenout = cindex.c_int(lenout)
    column = stypes.strtocharpoint(lenout)
    attdsc = stypes.SpiceEKAttDsc()
    libspice.ekcii_c(table, cindex, lenout, column, ctypes.byref(attdsc))
    return column.value, attdsc


def ekcls(handle):
    #Todo: test ekcls
    handle = ctypes.c_int(handle)
    libspice.ekcls_c(handle)
    pass


def ekdelr(handle, segno, recno):
    #Todo: test ekdelr
    handle = ctypes.c_int(handle)
    segno = ctypes.c_int(segno)
    recno = ctypes.c_int(recno)
    libspice.ekdelr_c(handle, segno, recno)
    pass


def ekffld(handle, segno, rcptrs):
    #Todo: test ekffld
    handle = ctypes.c_int(handle)
    segno = ctypes.c_int(segno)
    rcptrs = stypes.toIntVector(rcptrs)
    libspice.ekffld_c(handle, segno, ctypes.byref(rcptrs))
    pass


def ekfind(query, lenout):
    #Todo: test ekfind
    query = stypes.strtocharpoint(query)
    lenout = ctypes.c_int(lenout)
    nmrows = ctypes.c_int()
    error = ctypes.c_bool()
    errmsg = stypes.strtocharpoint(lenout)
    libspice.ekfind(query, lenout, ctypes.byref(nmrows), ctypes.byref(error), errmsg)
    return nmrows.value, error.value, errmsg


def ekgc(selidx, row, element, lenout):
    #Todo: test ekgc
    selidx = ctypes.c_int(selidx)
    row = ctypes.c_int(row)
    element = ctypes.c_int(element)
    lenout = ctypes.c_int(lenout)
    null = ctypes.c_bool()
    found = ctypes.c_bool()
    cdata = stypes.strtocharpoint(lenout)
    libspice.ekgc_c(selidx, row, element, lenout, cdata, null, found)
    return cdata.value, null.value, found.value


def ekgd(selidx, row, element):
    #Todo: test ekgd
    selidx = ctypes.c_int(selidx)
    row = ctypes.c_int(row)
    element = ctypes.c_int(element)
    ddata = ctypes.c_double()
    null = ctypes.c_bool()
    found = ctypes.c_bool()
    libspice.ekgd_c(selidx, row, element, ctypes.byref(ddata), ctypes.byref(null), ctypes.byref(found))
    return ddata.value, null.value, found.value


def ekgi(selidx, row, element):
    #Todo: test ekgi
    selidx = ctypes.c_int(selidx)
    row = ctypes.c_int(row)
    element = ctypes.c_int(element)
    idata = ctypes.c_double()
    null = ctypes.c_bool()
    found = ctypes.c_bool()
    libspice.ekgi_c(selidx, row, element, ctypes.byref(idata), ctypes.byref(null), ctypes.byref(found))
    return idata.value, null.value, found.value


def ekifld(handle, tabnam, ncols, nrows, cnmlen, cnames, declen, decls):
    #Todo: test ekifld
    handle = ctypes.c_int(handle)
    recptrs = stypes.intVector(nrows)
    tabnam = stypes.strtocharpoint(tabnam)
    cnames = stypes.listToCharArrayPtr(cnames, xLen=ncols, yLen=cnmlen)
    decls = stypes.listToCharArrayPtr(decls, xLen=ncols, yLen=declen)
    ncols = ctypes.c_int(ncols)
    nrows = ctypes.c_int(nrows)
    cnmlen = ctypes.c_int(cnmlen)
    declen = ctypes.c_int(declen)
    segno = ctypes.c_int()
    libspice.ekifld_c(handle, tabnam, ncols, nrows, cnmlen, cnames, declen, decls, ctypes.byref(segno), ctypes.byref(recptrs))
    return segno.value, stypes.vectorToList(recptrs)


def ekinsr(handle, segno, recno):
    #Todo: test ekinsr
    handle = ctypes.c_int(handle)
    segno = ctypes.c_int(segno)
    recno = ctypes.c_int(recno)
    libspice.ekinsr_c(handle, segno, recno)
    pass


def eklef(fname):
    #Todo: test eklef
    fname = stypes.strtocharpoint(fname)
    handle = ctypes.c_int()
    libspice.eklef_c(fname, handle)
    pass


def eknelt(selidx, row):
    #Todo: test eknelt
    selidx = ctypes.c_int(selidx)
    row = ctypes.c_int(row)
    return libspice.eknelt_c(selidx, row)


def eknseg(handle):
    #todo: test eknseg
    handle = ctypes.c_int(handle)
    return libspice.eknseg_c(handle)


def ekntab():
    #Todo: test ekntab
    n = ctypes.c_int()
    libspice.ekntab_c(ctypes.byref(n))
    return n.value


def ekopn(fname, ifname, ncomch):
    #Todo: test ekopn
    fname = stypes.strtocharpoint(fname)
    ifname = stypes.strtocharpoint(ifname)
    ncomch = ctypes.c_int(ncomch)
    handle = ctypes.c_int()
    libspice.ekopn_c(fname, ifname, ncomch, handle)
    return handle.value


def ekopr(fname):
    #Todo: test ekopr
    fname = stypes.strtocharpoint(fname)
    handle = ctypes.c_int()
    libspice.ekopr_c(fname, ctypes.byref(handle))
    return handle.value


def ekpos():
    #Todo: test ekpos
    handle = ctypes.c_int()
    libspice.ekpos_c(ctypes.byref(handle))
    return handle.value


def ekopw(fname):
    #Todo: test ekopw
    fname = stypes.strtocharpoint(fname)
    handle = ctypes.c_int()
    libspice.ekopw_c(fname, ctypes.byref(handle))
    return handle.value


def ekpsel(query, msglen, tablen, collen):
    #Todo: test ekpsel
    query = stypes.strtocharpoint(query)
    msglen = ctypes.c_int(msglen)
    tablen = ctypes.c_int(tablen)
    collen = ctypes.c_int(collen)
    n = ctypes.c_int()
    xbegs = ctypes.c_int()
    xends = ctypes.c_int()
    xtypes = stypes.SpiceEKDataType()
    xclass = stypes.SpiceEKExprClass()
    tabs = stypes.charvector(100, 33)
    cols = stypes.charvector(100, 65)
    error = ctypes.c_bool()
    errmsg = stypes.strtocharpoint(msglen)
    libspice.ekpsel_c(query, msglen, tablen, collen, ctypes.byref(n), ctypes.byref(xbegs), ctypes.byref(xends), ctypes.byref(xtypes), ctypes.byref(xclass), ctypes.byref(tabs), ctypes.byref(cols), ctypes.byref(error), ctypes.byref(errmsg))
    return n.value, xbegs.value, xends.value, xtypes.value, xclass.value, stypes.vectorToList(tabs), stypes.vectorToList(cols), error.value, errmsg.value


def ekrcec(handle, segno, recno, column, lenout, nelts=3):
    #Todo: test ekrcec , possible new way to get back 2d char arrays
    handle = ctypes.c_int(handle)
    segno = ctypes.c_int(segno)
    recno = ctypes.c_int(recno)
    column = stypes.strtocharpoint(column)
    lenout = ctypes.c_int(lenout)
    nvals = ctypes.c_int()
    cvals = stypes.charvector(ndim=nelts, lenvals=lenout)
    isnull = ctypes.c_bool()
    libspice.ekrcec_c(handle, segno, recno, column, lenout, ctypes.byref(nvals), ctypes.byref(cvals), ctypes.byref(isnull))
    return nvals.value, stypes.vectorToList(cvals), isnull.value


def ekrced(handle, segno, recno, column):
    #Todo: test ekrced
    handle = ctypes.c_int(handle)
    segno = ctypes.c_int(segno)
    recno = ctypes.c_int(recno)
    column = stypes.strtocharpoint(column)
    nvals = ctypes.c_int()
    dvals = ctypes.POINTER(ctypes.c_double)  # array of length nvals
    isnull = ctypes.c_bool()
    libspice.ekrced_c(handle, segno, recno, column, ctypes.byref(nvals), ctypes.byref(dvals), ctypes.byref(isnull))
    return nvals.value, stypes.vectorToList(dvals), isnull.value


def ekrcei(handle, segno, recno, column):
    #Todo: test ekrcei
    handle = ctypes.c_int(handle)
    segno = ctypes.c_int(segno)
    recno = ctypes.c_int(recno)
    column = stypes.strtocharpoint(column)
    nvals = ctypes.c_int()
    ivals = ctypes.POINTER(ctypes.c_int)  # array of length nvals
    isnull = ctypes.c_bool()
    libspice.ekrcei_c(handle, segno, recno, column, ctypes.byref(nvals), ctypes.byref(ivals), ctypes.byref(isnull))
    return nvals.value, stypes.vectorToList(ivals), isnull.value


def ekssum(handle, segno):
    #Todo: test ekssum and spiceEKSegSum type
    handle = ctypes.c_int(handle)
    segno = ctypes.c_int(segno)
    segsum = stypes.SpiceEKSegSum()
    libspice.ekssum_c(handle, segno, ctypes.byref(segsum))
    return segsum


def ektnam(n, lenout):
    #Todo: test ektnam
    n = ctypes.c_int(n)
    lenout = ctypes.c_int(lenout)
    table = stypes.strtocharpoint(lenout)
    libspice.ektnam_c(n, lenout, table)
    return table.value


def ekucec(handle, segno, recno, column, nvals, vallen, cvals, isnull):
    #Todo: test ekucec
    handle = ctypes.c_int(handle)
    segno = ctypes.c_int(segno)
    recno = ctypes.c_int(recno)
    column = stypes.strtocharpoint(column)
    nvals = ctypes.c_int(nvals)
    vallen = ctypes.c_int(vallen)
    isnull = ctypes.c_bool(isnull)
    cvals = stypes.listToCharArrayPtr(cvals, xLen=vallen, yLen=nvals)
    libspice.ekucec_c(handle, segno, recno, column, nvals, vallen, cvals, isnull)
    pass


def ekuced(handle, segno, recno, column, nvals, dvals, isnull):
    #Todo: test ekucei
    handle = ctypes.c_int(handle)
    segno = ctypes.c_int(segno)
    recno = ctypes.c_int(recno)
    column = stypes.strtocharpoint(column)
    nvals = ctypes.c_int(nvals)
    isnull = ctypes.c_bool(isnull)
    dvals = stypes.toDoubleVector(dvals)
    libspice.ekuced_c(handle, segno, recno, column, nvals, ctypes.byref(dvals), isnull)
    pass


def ekucei(handle, segno, recno, column, nvals, ivals, isnull):
    #Todo: test ekucei
    handle = ctypes.c_int(handle)
    segno = ctypes.c_int(segno)
    recno = ctypes.c_int(recno)
    column = stypes.strtocharpoint(column)
    nvals = ctypes.c_int(nvals)
    isnull = ctypes.c_bool(isnull)
    ivals = stypes.toIntVector(ivals)
    libspice.ekucei_c(handle, segno, recno, column, nvals, ctypes.byref(ivals), isnull)
    pass


def ekuef(handle):
    #Todo: test ekuef
    handle = ctypes.c_int(handle)
    libspice.ekuef_c(handle)
    pass


def el2cgv(ellipse):
    #Todo: test el2cgv
    assert(isinstance(ellipse, stypes.Ellipse))
    center = stypes.doubleVector(3)
    smajor = stypes.doubleVector(3)
    sminor = stypes.doubleVector(3)
    libspice.el2cgv_c(ctypes.byref(ellipse), center, smajor, sminor)
    return stypes.vectorToList(center), stypes.vectorToList(smajor), stypes.vectorToList(sminor)


def elemc(item, inset):
    #Todo: test elemc
    assert isinstance(inset, stypes.SpiceCell)
    item = stypes.strtocharpoint(item)
    return libspice.elemc_c(item, ctypes.byref(inset))


def elemd(item, inset):
    #Todo: test elemd
    assert isinstance(inset, stypes.SpiceCell)
    item = ctypes.c_double(item)
    return libspice.elemd_c(item, ctypes.byref(inset))


def elemi(item, inset):
    #Todo: test elemi
    assert isinstance(inset, stypes.SpiceCell)
    item = ctypes.c_int(item)
    return libspice.elemi_c(item, ctypes.byref(inset))


def eqstr(a, b):
    #Todo: test eqstr
    return libspice.eqstr_c(stypes.strtocharpoint(a), stypes.strtocharpoint(b))


def erract(op, lenout, action=None):
    #erract works, new method for dealing with returned strings/buffers
    if action is None:
        action = ""
    lenout = ctypes.c_int(lenout)
    op = stypes.strtocharpoint(op)
    action = ctypes.create_string_buffer(str.encode(action), lenout.value)
    actionptr = ctypes.c_char_p(ctypes.addressof(action))
    libspice.erract_c(op, lenout, actionptr)
    return bytes.decode(actionptr.value)


def errch(marker, string):
    marker = stypes.strtocharpoint(marker)
    string = stypes.strtocharpoint(string)
    libspice.errch_c(marker, string)
    pass


def errdev(op, lenout, device):
    #Todo: test errdev
    lenout = ctypes.c_int(lenout)
    op = stypes.strtocharpoint(op)
    device = ctypes.create_string_buffer(str.encode(device), lenout.value)
    deviceptr = ctypes.c_char_p(ctypes.addressof(device))
    libspice.errdev_c(op, lenout, deviceptr)
    return bytes.decode(deviceptr.value)


def errdp(marker, number):
    #Todo: test errdb
    marker = stypes.strtocharpoint(marker)
    number = ctypes.c_double(number)
    libspice.errdb_c(marker, number)
    pass


def errint(marker, number):
    #Todo: test errint
    marker = stypes.strtocharpoint(marker)
    number = ctypes.c_int(number)
    libspice.errint_c(marker, number)
    pass


def errprt(op, lenout, inlist):
    #Todo: test errprt
    lenout = ctypes.c_int(lenout)
    op = stypes.strtocharpoint(op)
    inlist = ctypes.create_string_buffer(str.encode(inlist), lenout.value)
    inlistptr = ctypes.c_char_p(ctypes.addressof(inlist))
    libspice.errdev_c(op, lenout, inlistptr)
    return bytes.decode(inlistptr.value)


def esrchc(value, ndim, lenvals, array):
    #Todo: test esrchc
    value = stypes.strtocharpoint(value)
    array = stypes.listToCharArrayPtr(array, xLen=lenvals, yLen=ndim)
    ndim = ctypes.c_int(ndim)
    lenvals = ctypes.c_int(lenvals)
    return libspice.esrchc_c(value, ndim, lenvals, array)


def et2lst(et, body, lon, typein, timlen, ampmlen):
    #Todo: test et2lst
    et = ctypes.c_double(et)
    body = ctypes.c_int(body)
    lon = ctypes.c_double(lon)
    typein = stypes.strtocharpoint(typein)
    timlen = ctypes.c_int(timlen)
    ampmlen = ctypes.c_int(ampmlen)
    hr = ctypes.c_int()
    mn = ctypes.c_int()
    sc = ctypes.c_int()
    time = stypes.strtocharpoint(timlen)
    ampm = stypes.strtocharpoint(ampmlen)
    libspice.et2lst(et, body, lon, typein, timlen, ampmlen, ctypes.byref(hr), ctypes.byref(mn), ctypes.byref(sc), time, ampm)
    return hr.value, mn.value, sc.value, time.value, ampm.value


def et2utc(et, formatStr, prec, lenout):
    #Todo: test et2utc
    et = ctypes.c_double(et)
    prec = ctypes.c_int(prec)
    lenout = ctypes.c_int(lenout)
    formatStr = stypes.strtocharpoint(formatStr)
    utcstr = stypes.strtocharpoint(lenout)
    libspice.et2utc_c(et, formatStr, prec, lenout, utcstr)
    return utcstr.value


def etcal(et, lenout):
    #Todo: test etcal
    et = ctypes.c_double(et)
    lenout = ctypes.c_int(lenout)
    string = stypes.strtocharpoint(lenout)
    libspice.etcal_c(et, lenout, string)
    return string.value


def eul2m(angle3, angle2, angle1, axis3, axis2, axis1):
    #Todo: test eul2m
    angle3 = ctypes.c_double(angle3)
    angle2 = ctypes.c_double(angle2)
    angle1 = ctypes.c_double(angle1)
    axis3 = ctypes.c_int(axis3)
    axis2 = ctypes.c_int(axis2)
    axis1 = ctypes.c_int(axis1)
    r = stypes.doubleMatrix()
    libspice.eul2m_c(angle3, angle2, angle1, axis3, axis2, axis1, r)
    return stypes.matrixToList(r)


def eul2xf(eulang, axisa, axisb, axisc):
    #Todo: eul2xf
    assert len(eulang) is 6
    eulang = stypes.toDoubleVector(eulang)
    axisa = ctypes.c_int(axisa)
    axisb = ctypes.c_int(axisb)
    axisc = ctypes.c_int(axisc)
    xform = stypes.doubleMatrix(x=6, y=6)
    libspice.eul2xf_c(eulang, axisa, axisb, axisc, xform)
    return stypes.matrixToList(xform)


def exists(fname):
    #Todo: test exists
    fname = stypes.strtocharpoint(fname)
    return libspice.exists_c(fname)


def expool(name):
    #Todo: test expool
    name = stypes.strtocharpoint(name)
    found = ctypes.c_bool()
    libspice.expool_c(name, found)
    return found.value


########################################################################################################################
# F


def failed():
    #todo: test failed
    return libspice.failed_c()


def frame(x):
    x = stypes.toDoubleVector(x)
    y = stypes.doubleVector(3)
    z = stypes.doubleVector(3)
    libspice.frame_c(x, y, z)
    return stypes.vectorToList(x), stypes.vectorToList(y), stypes.vectorToList(z)


def frinfo(frcode):
    #Todo: test frinfo
    frcode = ctypes.c_int(frcode)
    cent = ctypes.c_int()
    frclss = ctypes.c_int()
    clssid = ctypes.c_int()
    found = ctypes.c_bool()
    libspice.frinfo_c(frcode, ctypes.byref(cent), ctypes.byref(frclss), ctypes.byref(clssid), ctypes.byref(found))
    return cent.value, frclss.value, clssid.value, found.value


def frmnam(frcode, lenout):
    #Todo: test frmnam
    frcode = ctypes.c_int(frcode)
    lenout = ctypes.c_int(lenout)
    frname = stypes.strtocharpoint(lenout)
    libspice.frmnam_c(frcode, lenout, frname)
    return frname.value


def ftncls(unit):
    #Todo: close ftncls
    unit = ctypes.c_int(unit)
    libspice.ftncls_c(unit)
    pass


def furnsh(path):
    path = stypes.strtocharpoint(path)
    libspice.furnsh_c(path)
    pass

########################################################################################################################
# G


def gcpool(name, start, room, lenout):
    #Todo: test gcpool
    name = stypes.strtocharpoint(name)
    start = ctypes.c_int(start)
    room = ctypes.c_int(room)
    lenout = ctypes.c_int(lenout)
    n = ctypes.c_int()
    cvals = ctypes.c_void_p()  # not sure if this will work...
    found = ctypes.c_bool()
    libspice.gcpool_c(name, start, room, lenout, ctypes.byref(n), ctypes.byref(cvals), ctypes.byref(found))
    return n.value, cvals.value, found.value


def gdpool(name, start, room):
    #Todo: test gdpool works!
    name = stypes.strtocharpoint(name)
    start = ctypes.c_int(start)
    values = stypes.doubleVector(room)
    room = ctypes.c_int(room)
    n = ctypes.c_int()
    found = ctypes.c_bool()
    libspice.gdpool_c(name, start, room, ctypes.byref(n), ctypes.cast(values, ctypes.POINTER(ctypes.c_double)), ctypes.byref(found))
    return n.value, stypes.vectorToList(values), found.value


def georec(lon, lat, alt, re, f):
    #Todo: test georec
    lon = ctypes.c_double(lon)
    lat = ctypes.c_double(lat)
    alt = ctypes.c_double(alt)
    re = ctypes.c_double(re)
    f = ctypes.c_double(f)
    rectan = stypes.doubleVector(3)
    libspice.georec_c(lon, lat, alt, re, f, rectan)
    return stypes.vectorToList(rectan)


# getcml not really needed


def getelm(frstyr, lineln, lines):
    #Todo: test getelm
    frstyr = ctypes.c_int(frstyr)
    lineln = ctypes.c_int(lineln)
    lines = stypes.listToCharArrayPtr(lines, xLen=2, yLen=lineln)
    epoch = ctypes.c_double()
    elems = stypes.doubleVector(lineln)  # guess for length
    libspice.getelm_c(frstyr, lineln, ctypes.byref(lines), ctypes.byref(epoch), ctypes.byref(elems))


def getfat(file, arclen, typlen):
    #Todo: test getfat, or is this really needed at all?
    file = stypes.strtocharpoint(file)
    arclen = ctypes.c_int(arclen)
    typlen = ctypes.c_int(typlen)
    arch = stypes.strtocharpoint(arclen)
    rettype = stypes.strtocharpoint(typlen)
    libspice.getfat_c(file, arclen, typlen, arch, rettype)
    return arch.value, rettype.value


def getfov(instid, room, shapelen, framelen):
    #This is technically a hack, please fix so that room does something!
    instid = ctypes.c_int(instid)
    room = ctypes.c_int(room)
    shape = stypes.strtocharpoint(" "*shapelen)
    framen = stypes.strtocharpoint(" "*framelen)
    shapelen = ctypes.c_int(shapelen)
    framelen = ctypes.c_int(framelen)
    bsight = stypes.doubleVector(3)
    n = ctypes.c_int(0)
    bounds = stypes.doubleMatrix(x=3, y=4)
    libspice.getfov_c(instid, room, shapelen, framelen, shape, framen, bsight, ctypes.byref(n), bounds)
    return shape.value, framen.value, stypes.vectorToList(bsight), stypes.matrixToList(bounds)


def getmsg(option, lenout):
    #todo: test getmsg
    option = stypes.strtocharpoint(option)
    lenout = ctypes.c_int(lenout)
    msg = stypes.strtocharpoint(lenout)
    libspice.getmsg_c(option, lenout, msg)
    return msg.value


def gfbail():
    #todo: test gfbail. funny name
    return libspice.gfbail_c()


def gfclrh():
    #Todo: test gfclrh
    libspice.gfclrh_c()
    pass


def gfdist(target, abcorr, obsrvr, relate, refval, adjust, step, nintvls, cnfine):
    #Todo: test gfdist
    assert isinstance(cnfine, stypes.SpiceCell)
    assert cnfine.is_double()
    target = stypes.strtocharpoint(target)
    abcorr = stypes.strtocharpoint(abcorr)
    obsrvr = stypes.strtocharpoint(obsrvr)
    relate = stypes.strtocharpoint(relate)
    refval = ctypes.c_double(refval)
    adjust = ctypes.c_double(adjust)
    step = ctypes.c_double(step)
    nintvls = ctypes.c_int(nintvls)
    result = stypes.SPICEDOUBLE_CELL(cnfine.size)
    libspice.gfdist_c(target, abcorr, obsrvr, relate, refval, adjust, step, nintvls, ctypes.byref(cnfine), ctypes.byref(result))
    return cnfine, result


#gdevnt  callbacks? cells


#gffove  callbacks? cells


def gfinth(sigcode):
    #Todo: test gfinth
    sigcode = ctypes.c_int(sigcode)
    libspice.gfinth_c(sigcode)
    pass


#gfocce  callbacks? cells


def gfoclt_c(occtyp, front, fshape, fframe, back, bshape, bframe, abcorr, obsrvr, step, cnfine):
    #Todo: test gfoclt
    assert isinstance(cnfine, stypes.SpiceCell)
    assert cnfine.is_double()
    occtyp = stypes.strtocharpoint(occtyp)
    front = stypes.strtocharpoint(front)
    fshape = stypes.strtocharpoint(fshape)
    fframe = stypes.strtocharpoint(fframe)
    back = stypes.strtocharpoint(back)
    bshape = stypes.strtocharpoint(bshape)
    bframe = stypes.strtocharpoint(bframe)
    abcorr = stypes.strtocharpoint(abcorr)
    obsrvr = stypes.strtocharpoint(obsrvr)
    step = ctypes.c_double(step)
    result = stypes.SPICEDOUBLE_CELL(cnfine.size)
    libspice.gfoclt_c(occtyp, front, fshape, fframe, back, bshape, bframe, abcorr, obsrvr, step, ctypes.byref(cnfine), ctypes.byref(result))
    return cnfine, result


def gfposc(target, inframe, abcorr, obsrvr, crdsys, coord, relate, refval, adjust, step, nintvals, cnfine):
    #Todo: test gfposc
    assert isinstance(cnfine, stypes.SpiceCell)
    assert cnfine.is_double()
    target = stypes.strtocharpoint(target)
    inframe = stypes.strtocharpoint(inframe)
    abcorr = stypes.strtocharpoint(abcorr)
    obsrvr = stypes.strtocharpoint(obsrvr)
    crdsys = stypes.strtocharpoint(crdsys)
    coord = stypes.strtocharpoint(coord)
    relate = stypes.strtocharpoint(relate)
    refval = ctypes.c_double(refval)
    adjust = ctypes.c_double(adjust)
    step = ctypes.c_double(step)
    nintvals = ctypes.c_int(nintvals)
    result = stypes.SPICEDOUBLE_CELL(cnfine.size)
    libspice.gfposc_c(target, inframe, abcorr, obsrvr, crdsys, coord, relate, refval, adjust, step, nintvals, ctypes.byref(cnfine), ctypes.byref(result))
    return cnfine, result


def gfrefn(t1, t2, s1, s2):
    #Todo: test gfrefn
    t1 = ctypes.c_double(t1)
    t2 = ctypes.c_double(t2)
    s1 = ctypes.c_bool(s1)
    s2 = ctypes.c_bool(s2)
    t = ctypes.c_bool()
    libspice.gfrefn_c(t1, t2, s1, s2, ctypes.byref(t))
    return t.value


def gfrepf():
    #Todo: test gfrepf
    libspice.gfrepf_c()
    pass


def gfrepi(window, begmss, endmss):
    #Todo: test gfrepi
    assert isinstance(window, stypes.SpiceCell)
    assert window.is_double()
    begmss = stypes.strtocharpoint(begmss)
    endmss = stypes.strtocharpoint(endmss)
    libspice.gfrepi_c(ctypes.byref(window), begmss, endmss)
    pass


def gfrepu(ivbeg, ivend, time):
    #Todo: test gfrepu
    ivbeg = ctypes.c_double(ivbeg)
    ivend = ctypes.c_double(ivend)
    time = ctypes.c_double(time)
    libspice.gfrepu_c(ivbeg, ivend, time)
    pass


def gfrfov(inst, raydir, rframe, abcorr, obsrvr, step, cnfine):
    #Todo: test gfrfov
    assert isinstance(cnfine, stypes.SpiceCell)
    assert cnfine.is_double()
    inst = stypes.strtocharpoint(inst)
    raydir = stypes.toDoubleVector(raydir)
    rframe = stypes.strtocharpoint(rframe)
    abcorr = stypes.strtocharpoint(abcorr)
    obsrvr = stypes.strtocharpoint(obsrvr)
    step = ctypes.c_double(step)
    result = stypes.SPICEDOUBLE_CELL(cnfine.size)
    libspice.gfrfov_c(inst, raydir, rframe, abcorr, obsrvr, step, ctypes.byref(cnfine), ctypes.byref(result))
    return cnfine, result


def gfrr(target, abcorr, obsrvr, relate, refval, adjust, step, nintvals, cnfine):
    #Todo: test gfrr
    assert isinstance(cnfine, stypes.SpiceCell)
    assert cnfine.is_double()
    target = stypes.strtocharpoint(target)
    abcorr = stypes.strtocharpoint(abcorr)
    obsrvr = stypes.strtocharpoint(obsrvr)
    relate = stypes.strtocharpoint(relate)
    refval = ctypes.c_double(refval)
    adjust = ctypes.c_double(adjust)
    step = ctypes.c_double(step)
    nintvals = ctypes.c_int(nintvals)
    result = stypes.SPICEDOUBLE_CELL(cnfine.size)
    libspice.gfrr_c(target, abcorr, obsrvr, relate, refval, adjust, step, nintvals, ctypes.byref(cnfine), ctypes.byref(result))
    return cnfine, result


def gfsep(targ1, shape1, inframe1, targ2, shape2, inframe2, abcorr, obsrvr, relate, refval, adjust, step, nintvals, cnfine):
    #Todo: test gfsep
    assert isinstance(cnfine, stypes.SpiceCell)
    assert cnfine.is_double()
    targ1 = stypes.strtocharpoint(targ1)
    shape1 = stypes.strtocharpoint(shape1)
    inframe1 = stypes.strtocharpoint(inframe1)
    targ2 = stypes.strtocharpoint(targ2)
    shape2 = stypes.strtocharpoint(shape2)
    inframe2 = stypes.strtocharpoint(inframe2)
    abcorr = stypes.strtocharpoint(abcorr)
    obsrvr = stypes.strtocharpoint(obsrvr)
    relate = stypes.strtocharpoint(relate)
    refval = ctypes.c_double(refval)
    adjust = ctypes.c_double(adjust)
    step = ctypes.c_double(step)
    nintvals = ctypes.c_int(nintvals)
    result = stypes.SPICEDOUBLE_CELL(cnfine.size)
    libspice.gfsep_c(targ1, shape1, inframe1, targ2, shape2, inframe2, abcorr, obsrvr, relate, refval, adjust, step, nintvals, ctypes.byref(cnfine), ctypes.byref(result))
    return cnfine, result


def gfsntc(target, fixref, method, abcorr, obsrvr, dref, dvec, crdsys, coord, relate, refval, adjust, step, nintvals, cnfine):
    #Todo: test gfsntc
    assert isinstance(cnfine, stypes.SpiceCell)
    assert cnfine.is_double()
    target = stypes.strtocharpoint(target)
    fixref = stypes.strtocharpoint(fixref)
    method = stypes.strtocharpoint(method)
    abcorr = stypes.strtocharpoint(abcorr)
    obsrvr = stypes.strtocharpoint(obsrvr)
    dref = stypes.strtocharpoint(dref)
    dvec = stypes.toDoubleVector(dvec)
    crdsys = stypes.strtocharpoint(crdsys)
    coord = stypes.strtocharpoint(coord)
    relate = stypes.strtocharpoint(relate)
    refval = ctypes.c_double(refval)
    adjust = ctypes.c_double(adjust)
    step = ctypes.c_double(step)
    nintvals = ctypes.c_int(nintvals)
    result = stypes.SPICEDOUBLE_CELL(cnfine.size)
    libspice.gfsntc_c(target, fixref, method, abcorr, obsrvr, dref, dvec, crdsys, coord, relate, refval, adjust, step, nintvals, ctypes.byref(cnfine), ctypes.byref(result))
    return cnfine, result


def gfsstp(step):
    #Todo: test gfsstp
    step = ctypes.c_double(step)
    libspice.gfsstp_c(step)
    pass


def gfstep(time):
    #Todo: test gfstep
    time = ctypes.c_double(time)
    step = ctypes.c_double()
    libspice.gfstep_c(time, ctypes.byref(step))
    return step.value


def gfsubc(target, fixref, method, abcorr, obsrvr, crdsys, coord, relate, refval, adjust, step, nintvals, cnfine):
    #Todo: test gfsubc
    assert isinstance(cnfine, stypes.SpiceCell)
    assert cnfine.is_double()
    target = stypes.strtocharpoint(target)
    fixref = stypes.strtocharpoint(fixref)
    method = stypes.strtocharpoint(method)
    abcorr = stypes.strtocharpoint(abcorr)
    obsrvr = stypes.strtocharpoint(obsrvr)
    crdsys = stypes.strtocharpoint(crdsys)
    coord = stypes.strtocharpoint(coord)
    relate = stypes.strtocharpoint(relate)
    refval = ctypes.c_double(refval)
    adjust = ctypes.c_double(adjust)
    step = ctypes.c_double(step)
    nintvals = ctypes.c_int(nintvals)
    result = stypes.SPICEDOUBLE_CELL(cnfine.size)
    libspice.gfsubc_c(target, fixref, method, abcorr, obsrvr, crdsys, coord, relate, refval, adjust, step, nintvals, ctypes.byref(cnfine), ctypes.byref(result))


def gftfov(inst, target, tshape, tframe, abcorr, obsrvr, step, cnfine):
    #Todo: test gftfov
    assert isinstance(cnfine, stypes.SpiceCell)
    assert cnfine.is_double()
    target = stypes.strtocharpoint(target)
    tshape = stypes.strtocharpoint(tshape)
    tframe = stypes.strtocharpoint(tframe)
    abcorr = stypes.strtocharpoint(abcorr)
    obsrvr = stypes.strtocharpoint(obsrvr)
    step = ctypes.c_double(step)
    result = stypes.SPICEDOUBLE_CELL(cnfine.size)
    libspice.gftfov_c(inst, target, tshape, tframe, abcorr, obsrvr, step, ctypes.byref(cnfine), ctypes.byref(result))


#gfuds has cell types and more


def gipool(name, start, room):
    #Todo: fix gipool room isn't doing anything
    name = stypes.strtocharpoint(name)
    start = ctypes.c_int(start)
    room = ctypes.c_int(room)
    n = ctypes.c_int()
    ivals = ctypes.c_int()
    found = ctypes.c_bool()
    libspice.gipool_c(name, start, room, ctypes.byref(n), ctypes.byref(ivals), ctypes.byref(found))
    return n.value, ivals.value, found.value


def gnpool(name, start, room, lenout):
    #Todo: test gnpool
    name = stypes.strtocharpoint(name)
    start = ctypes.c_int(start)
    kvars = stypes.charvector(room, lenout)
    room = ctypes.c_int(room)
    lenout = ctypes.c_int(lenout)
    n = ctypes.c_int()
    found = ctypes.c_bool()
    libspice.gnpool_c(name, start, room, lenout, ctypes.byref(n), kvars, ctypes.byref(found))
    return n.value, stypes.vectorToList(kvars), found.value


########################################################################################################################
# H


def halfpi():
    return libspice.halfpi_c()


def hx2dp(string, lenout):
    #Todo: test hx2dp
    string = stypes.strtocharpoint(string)
    lenout = ctypes.c_int(lenout)
    errmsg = stypes.strtocharpoint(lenout)
    number = ctypes.c_int()
    error = ctypes.c_bool()
    libspice.hx2dp_c(string, lenout, ctypes.byref(number), ctypes.byref(error), errmsg)
    return number.value, error.value, errmsg


########################################################################################################################
# I


def ident():
    matrix = stypes.doubleMatrix()
    libspice.ident_c(matrix)
    return stypes.matrixToList(matrix)


def illum(target, et, abcorr, obsrvr, spoint):
    #Todo: test illum
    target = stypes.strtocharpoint(target)
    et = ctypes.c_double(et)
    abcorr = stypes.strtocharpoint(abcorr)
    obsrvr = stypes.strtocharpoint(obsrvr)
    spoint = stypes.toDoubleVector(spoint)
    phase = ctypes.c_double(0)
    solar = ctypes.c_double(0)
    emissn = ctypes.c_double(0)
    libspice.illum_c(target, et, abcorr, obsrvr, spoint, ctypes.byref(phase), ctypes.byref(solar), ctypes.byref(emissn))
    return phase.value, solar.value, emissn.value


def ilumin(method, target, et, fixref, abcorr, obsrvr, spoint):
    method = stypes.strtocharpoint(method)
    target = stypes.strtocharpoint(target)
    et = ctypes.c_double(et)
    fixref = stypes.strtocharpoint(fixref)
    abcorr = stypes.strtocharpoint(abcorr)
    obsrvr = stypes.strtocharpoint(obsrvr)
    spoint = stypes.toDoubleVector(spoint)
    trgepc = ctypes.c_double(0)
    srfvec = stypes.doubleVector(3)
    phase = ctypes.c_double(0)
    solar = ctypes.c_double(0)
    emissn = ctypes.c_double(0)
    libspice.ilumin_c(method, target, et, fixref, abcorr, obsrvr, spoint, ctypes.byref(trgepc),
              srfvec, ctypes.byref(phase), ctypes.byref(solar), ctypes.byref(emissn))
    return trgepc.value, stypes.vectorToList(srfvec), phase.value, solar.value, emissn.value


def inedpl(a, b, c, plane):
    #Todo: test inedpl
    assert (isinstance(plane, stypes.Plane))
    ellipse = stypes.Ellipse()
    a = ctypes.c_double(a)
    b = ctypes.c_double(b)
    c = ctypes.c_double(c)
    found = ctypes.c_bool()
    libspice.inedpl_c(a, b, c, ctypes.byref(plane), ctypes.byref(ellipse), ctypes.byref(found))
    return ellipse, found.value


def inelpl(ellips, plane):
    #Todo: test inelpl
    assert(isinstance(plane, stypes.Plane))
    assert(isinstance(ellips, stypes.Ellipse))
    nxpts = ctypes.c_int()
    xpt1 = stypes.doubleVector(3)
    xpt2 = stypes.doubleVector(3)
    libspice.inelpl_c(ctypes.byref(ellips), ctypes.byref(plane), ctypes.byref(nxpts), xpt1, xpt2)
    return nxpts.value, stypes.vectorToList(xpt1), stypes.vectorToList(xpt2)


def inrypl(vertex, direct, plane):
    #Todo: test inrypl
    assert(isinstance(plane, stypes.Plane))
    vertex = stypes.toDoubleVector(vertex)
    direct = stypes.toDoubleVector(direct)
    nxpts = ctypes.c_int()
    xpt = stypes.doubleVector(3)
    libspice.inrypl_c(vertex, direct, ctypes.byref(plane), ctypes.byref(nxpts), xpt)
    return nxpts.value, stypes.vectorToList(xpt)


def insrtc(item, inset):
    #Todo: test instrc
    assert isinstance(inset, stypes.SpiceCell)
    item = stypes.strtocharpoint(item)
    libspice.instri_c(item, ctypes.byref(inset))
    pass


def insrtd(item, inset):
    #Todo: test instrd
    assert isinstance(inset, stypes.SpiceCell)
    item = ctypes.c_double(item)
    libspice.instrd_c(item, ctypes.byref(inset))
    pass


def insrti(item, inset):
    #Todo: test instri
    assert isinstance(inset, stypes.SpiceCell)
    item = ctypes.c_int(item)
    libspice.instri_c(item, ctypes.byref(inset))
    pass


def inter(a, b):
    #Todo: test inter, this cell handleing may work for copy.
    assert isinstance(a, stypes.SpiceCell)
    assert isinstance(b, stypes.SpiceCell)
    assert a.dtype == b.dtype
    assert a.dtype == 0 or a.dtype == 1 or a.dtype == 2
    if a.dtype is 0:
        c = stypes.SPICECHAR_CELL(a.size, a.length)
    if a.dtype is 1:
        c = stypes.SPICEDOUBLE_CELL(a.size)
    elif a.dtype is 2:
        c = stypes.SPICEINT_CELL(a.size)
    else:
        raise NotImplementedError
    libspice.inter_c(ctypes.byref(a), ctypes.byref(b), ctypes.byref(c))
    return c


def intmax():
    return libspice.intmax_c()


def intmin():
    return libspice.intmin_c()


def invert(m):
    #Todo: test invert
    m = stypes.listtodoublematrix(m)
    mout = stypes.doubleMatrix()
    libspice.invert_c(m, mout)
    return stypes.matrixToList(mout)


def invort(m):
    #Todo: test invort
    m = stypes.listtodoublematrix(m)
    mout = stypes.doubleMatrix()
    libspice.invort_c(m, mout)
    return stypes.matrixToList(mout)


def isordv(array, n):
    #todo: test isordv
    array = stypes.toIntVector(array)
    n = ctypes.c_int(n)
    return libspice.isordv_c(array, n)


def isrchc(value, ndim, lenvals, array):
    #Todo: test isrchc
    value = stypes.strtocharpoint(value)
    array = stypes.listToCharArrayPtr(array, xLen=lenvals, yLen=ndim)
    ndim = ctypes.c_int(ndim)
    lenvals = ctypes.c_int(lenvals)
    return libspice.isrchc_c(value, ndim, lenvals, array)


def isrchd(value, ndim, array):
    #todo: test isrchd
    value = ctypes.c_int(value)
    ndim = ctypes.c_int(ndim)
    array = stypes.toDoubleVector(array)
    return libspice.isrchd_c(value, ndim, array)


def isrchi(value, ndim, array):
    #todo: test isrchi
    value = ctypes.c_int(value)
    ndim = ctypes.c_int(ndim)
    array = stypes.toIntVector(array)
    return libspice.isrchi_c(value, ndim, array)


def isrot(m, ntol, dtol):
    #todo: test isrot
    m = stypes.listtodoublematrix(m)
    ntol = ctypes.c_double(ntol)
    dtol = ctypes.c_double(dtol)
    return libspice.isrot_c(m, ntol, dtol)


def iswhsp(string):
    #todo: test iswhsp
    string = stypes.strtocharpoint(string)
    return libspice.iswhsp_c(string)


########################################################################################################################
# J


def j1900():
    return libspice.j1900_c()


def j1950():
    return libspice.j1950_c()


def j2000():
    return libspice.j2000_c()


def j2100():
    return libspice.j2100_c()


def jyear():
    return libspice.jyear_c()
########################################################################################################################
# K


def kclear():
    libspice.kclear_c()
    pass


def kdata(which, kind, fillen, typlen, srclen):
    #Todo: test kdata
    which = ctypes.c_int(which)
    kind = stypes.strtocharpoint(kind)
    fillen = ctypes.c_int(fillen)
    typlen = ctypes.c_int(typlen)
    srclen = ctypes.c_int(srclen)
    file = stypes.strtocharpoint(" " * fillen.value)
    filtyp = stypes.strtocharpoint(" " * typlen.value)
    source = stypes.strtocharpoint(" " * srclen.value)
    handle = ctypes.c_int()
    found = ctypes.c_bool()
    libspice.kdata_c(which, kind, fillen, typlen, srclen, file, filtyp, source, ctypes.byref(handle), ctypes.byref(found))
    return file.value, filtyp.value, source.value, handle.value, found.value


def kinfo(file, typlen, srclen):
    #todo: test kinfo
    typlen = ctypes.c_int(typlen)
    srclen = ctypes.c_int(srclen)
    file = stypes.strtocharpoint(file)
    filtyp = stypes.strtocharpoint(" " * typlen.value)
    source = stypes.strtocharpoint(" " * srclen.value)
    handle = ctypes.c_int()
    found = ctypes.c_bool()
    libspice.kinfo_c(file, typlen, srclen, filtyp, source, ctypes.byref(handle), ctypes.byref(found))
    return filtyp.value, source.value, handle.value, found.value


def ktotal(kind):
    kind = stypes.strtocharpoint(kind)
    count = ctypes.c_int()
    libspice.ktotal_c(kind, ctypes.byref(count))
    return count.value


def kxtrct(keywd, termlen, terms, nterms, stringlen, substrlen, string):
    #Todo: test kxtrct
    keywd = stypes.strtocharpoint(keywd)
    termlen = ctypes.c_int(termlen)
    terms = stypes.listToCharArrayPtr(terms, xlen=stringlen, yLen=nterms)
    nterms = ctypes.c_int(nterms)
    string = stypes.strtocharpoint(string, inlen=stringlen)
    substr = stypes.strtocharpoint(" "*substrlen, inlen=substrlen)
    stringlen = ctypes.c_int(stringlen)
    substrlen = ctypes.c_int(substrlen)
    found = ctypes.c_bool()
    libspice.kxtrct_c(keywd, termlen, terms, nterms, stringlen, substrlen, ctypes.byref(string), ctypes.byref(found), ctypes.byref(substr))
    return string.value, found.value, substr.value


########################################################################################################################
# L


def lastnb(string):
    #Todo: test lastnb
    string = stypes.strtocharpoint(string)
    return libspice.lastnb_c(string)


def latcyl(radius, lon, lat):
    #Todo: test latcyl
    radius = ctypes.c_double(radius)
    lon = ctypes.c_double(lon)
    lat = ctypes.c_double(lat)
    r = ctypes.c_double()
    lonc = ctypes.c_double()
    z = ctypes.c_double()
    libspice.latcyl_c(radius, lon, lat, ctypes.byref(r), ctypes.byref(lonc), ctypes.byref(z))
    return r.value, lonc.value, z.value


def latrec(radius, longitude, latitude):
    #Todo: test latrec
    radius = ctypes.c_double(radius)
    longitude = ctypes.c_double(longitude)
    latitude = ctypes.c_double(latitude)
    rectan = stypes.doubleVector(3)
    libspice.latrec_c(radius, longitude, latitude, rectan)
    return stypes.vectorToList(rectan)


def latsph(radius, lon, lat):
    #Todo: test latsph
    radius = ctypes.c_double(radius)
    lon = ctypes.c_double(lon)
    lat = ctypes.c_double(lat)
    rho = ctypes.c_double()
    colat = ctypes.c_double()
    lons = ctypes.c_double()
    libspice.latsph_c(radius, lon, lat, ctypes.byref(rho), ctypes.byref(colat), ctypes.byref(lons))
    return rho.value, colat.value, lons.value


def lcase(instr, lenout):
    #Todo: test lcase
    instr = stypes.strtocharpoint(instr)
    lenout = ctypes.c_int(lenout)
    outstr = stypes.strtocharpoint(lenout)
    libspice.lcase_c(instr, lenout, outstr)
    return outstr.value


def ldpool(filename):
    filename = stypes.strtocharpoint(filename)
    libspice.ldpool_c(filename)
    pass


def lmpool(cvals, lenvals, n):
    #Todo: test lmpool
    lenvals = ctypes.c_int(lenvals)
    n = ctypes.c_int(n)
    cvals = stypes.listToCharArrayPtr(cvals, xLen=lenvals, yLen=n)
    libspice.lmpool_c(cvals, lenvals, n)
    pass


def lparse(inlist, delim, nmax, lenout):
    #Todo: test lparse
    inlist = stypes.strtocharpoint(inlist)
    delim = stypes.strtocharpoint(delim)
    items = stypes.charvector(nmax, lenout)
    nmax = ctypes.c_int(nmax)
    lenout = ctypes.c_int(lenout)
    n = ctypes.c_int()
    libspice.lparse_c(inlist, delim, nmax, lenout, ctypes.byref(n), ctypes.byref(items))
    return n.value, stypes.vectorToList(items)


def lparsm(inlist, delims, nmax, lenout):
    #Todo: test lparsm
    inlist = stypes.strtocharpoint(inlist)
    delims = stypes.strtocharpoint(delims)
    items = stypes.charvector(nmax, lenout)
    nmax = ctypes.c_int(nmax)
    lenout = ctypes.c_int(lenout)
    n = ctypes.c_int()
    libspice.lparsm_c(inlist, delims, nmax, lenout, ctypes.byref(n), ctypes.byref(items))
    return n.value, stypes.vectorToList(items)


def lparss(inlist, delims, NMAX=20, LENGTH=50):
    #todo: test lparss, not working exactly
    inlist = stypes.strtocharpoint(inlist)
    delims = stypes.strtocharpoint(delims)
    returnSet = stypes.SPICECHAR_CELL(NMAX, LENGTH)
    libspice.lparss_c(inlist, delims, ctypes.byref(returnSet))
    return returnSet


def lspcn(body, et, abcorr):
    #Todo: test lspcn
    body = stypes.strtocharpoint(body)
    et = ctypes.c_double(et)
    abcorr = stypes.strtocharpoint(abcorr)
    return libspice.lspcn_c(body, et, abcorr)


def ltime(etobs, obs, direct, targ):
    #Todo: test ltime
    etobs = ctypes.c_double(etobs)
    obs = ctypes.c_int(obs)
    direct = stypes.strtocharpoint(direct)
    targ = ctypes.c_int(targ)
    ettarg = ctypes.c_double()
    elapsd = ctypes.c_double()
    libspice.ltime_c(etobs, obs, direct, targ, ctypes.byref(ettarg), ctypes.byref(elapsd))
    return ettarg, elapsd


def lstlec(string, n, lenvals, array):
    #Todo: Test lstlec
    string = stypes.strtocharpoint(string)
    array = stypes.listToCharArrayPtr(array, xLen=lenvals, yLen=n)
    n = ctypes.c_int(n)
    lenvals = ctypes.c_int(lenvals)
    return libspice.lstlec_c(string, n, lenvals, array)


def lstled(x, n, array):
    #Todo: test lstlei
    array = stypes.toDoubleVector(array)
    x = ctypes.c_double(x)
    n = ctypes.c_int(n)
    return libspice.lstled_c(x, n, array)


def lstlei(x, n, array):
    #Todo: test lstlei
    array = stypes.toIntVector(array)
    x = ctypes.c_int(x)
    n = ctypes.c_int(n)
    return libspice.lstlei_c(x, n, array)


def lstltc(string, n, lenvals, array):
    #WORKS!
    string = stypes.strtocharpoint(string)
    array = stypes.listToCharArrayPtr(array, xLen=lenvals, yLen=n)
    n = ctypes.c_int(n)
    lenvals = ctypes.c_int(lenvals)
    return libspice.lstltc_c(string, n, lenvals, array)


def lstltd(x, n, array):
    #Todo: test lstlti
    array = stypes.toDoubleVector(array)
    x = ctypes.c_double(x)
    n = ctypes.c_int(n)
    return libspice.lstltd_c(x, n, array)


def lstlti(x, n, array):
    #Todo: test lstlti
    array = stypes.toIntVector(array)
    x = ctypes.c_int(x)
    n = ctypes.c_int(n)
    return libspice.lstlti_c(x, n, array)


def lx4dec(string, first):
    #Todo: test lx4dec
    string = stypes.strtocharpoint(string)
    first = ctypes.c_int(first)
    last = ctypes.c_int()
    nchar = ctypes.c_int()
    libspice.lx4dec_c(string, first, ctypes.byref(last), ctypes.byref(nchar))
    return last.value, nchar.value


def lx4num(string, first):
    #Todo: test lx4num
    string = stypes.strtocharpoint(string)
    first = ctypes.c_int(first)
    last = ctypes.c_int()
    nchar = ctypes.c_int()
    libspice.lx4num_c(string, first, ctypes.byref(last), ctypes.byref(nchar))
    return last.value, nchar.value


def lx4sgn(string, first):
    #Todo: test lx4sgn
    string = stypes.strtocharpoint(string)
    first = ctypes.c_int(first)
    last = ctypes.c_int()
    nchar = ctypes.c_int()
    libspice.lx4sgn_c(string, first, ctypes.byref(last), ctypes.byref(nchar))
    return last.value, nchar.value


def lx4uns(string, first):
    #Todo: test lx4uns
    string = stypes.strtocharpoint(string)
    first = ctypes.c_int(first)
    last = ctypes.c_int()
    nchar = ctypes.c_int()
    libspice.lx4uns_c(string, first, ctypes.byref(last), ctypes.byref(nchar))
    return last.value, nchar.value


def lxqstr(string, qchar, first):
    #Todo: test lxqstr
    string = stypes.strtocharpoint(string)
    qchar = ctypes.c_char(qchar)
    first = ctypes.c_int(first)
    last = ctypes.c_int()
    nchar = ctypes.c_int()
    libspice.lxqstr_c(string, qchar, first, ctypes.byref(last), ctypes.byref(nchar))
    return last.value, nchar.value


########################################################################################################################
# M


def m2eul(r, axis3, axis2, axis1):
    #todo: test m2eul
    r = stypes.listtodoublematrix(r)
    axis3 = ctypes.c_int(axis3)
    axis2 = ctypes.c_int(axis2)
    axis1 = ctypes.c_int(axis1)
    angle3 = ctypes.c_double()
    angle2 = ctypes.c_double()
    angle1 = ctypes.c_double()
    libspice.m2eul_c(r, axis3, axis2, axis1, ctypes.byref(angle3), ctypes.byref(angle2), ctypes.byref(angle1))
    return angle3.value, angle2.value, angle1.value


def m2q(r):
    #Todo: test m2q
    r = stypes.listtodoublematrix(r)
    q = stypes.doubleVector(4)
    libspice.m2q_c(r, q)
    return stypes.vectorToList(q)


def matchi(string, templ, wstr, wchr):
    #Todo: test matchi
    string = stypes.strtocharpoint(string)
    templ = stypes.strtocharpoint(templ)
    wstr = ctypes.c_char(wstr.encode(encoding='UTF-8'))
    wchr = ctypes.c_char(wchr.encode(encoding='UTF-8'))
    return libspice.matchi_c(string, templ, wstr, wchr)


def matchw(string, templ, wstr, wchr):
    #Todo: test matchw
    string = stypes.strtocharpoint(string)
    templ = stypes.strtocharpoint(templ)
    wstr = ctypes.c_char(wstr.encode(encoding='UTF-8'))
    wchr = ctypes.c_char(wchr.encode(encoding='UTF-8'))
    return libspice.matchw_c(string, templ, wstr, wchr)


#skiping for now maxd_c, odd as arguments must be parsed and not really important


#skiping for now maxi_c, odd as arguments must be parsed and not really important


def mequ(m1):
    m1 = stypes.listtodoublematrix(m1)
    mout = stypes.doubleMatrix()
    libspice.mequ_c(m1, mout)
    return stypes.matrixToList(mout)


def mequg(m1, nr, nc):
    m1 = stypes.listtodoublematrix(m1, x=nc, y=nr)
    mout = stypes.doubleMatrix(x=nc, y=nr)
    nc = ctypes.c_int(nc)
    nr = ctypes.c_int(nr)
    libspice.mequg_c(m1, nc, nr, mout)
    return stypes.matrixToList(mout)


#skiping for now mind_c, odd as arguments must be parsed and not really important


#skiping for now mini_c, odd as arguments must be parsed and not really important


def mtxm(m1, m2):
    m1 = stypes.listtodoublematrix(m1)
    m2 = stypes.listtodoublematrix(m2)
    mout = stypes.doubleMatrix()
    libspice.mtxm_c(m1, m2, mout)
    return stypes.matrixToList(mout)


def mtxmg(m1, m2, ncol1, nr1r2, ncol2):
    m1 = stypes.listtodoublematrix(m1, x=ncol1, y=nr1r2)
    m2 = stypes.listtodoublematrix(m2, x=ncol2, y=nr1r2)
    mout = stypes.doubleMatrix(x=ncol2, y=ncol1)
    ncol1 = ctypes.c_int(ncol1)
    nr1r2 = ctypes.c_int(nr1r2)
    ncol2 = ctypes.c_int(ncol2)
    libspice.mtxmg_c(m1, m2, ncol1, nr1r2, ncol2, mout)
    return stypes.matrixToList(mout)


def mtxv(m1, vin):
    #Todo: test mtxv
    m1 = stypes.listtodoublematrix(m1)
    vin = stypes.toDoubleVector(vin)
    vout = stypes.doubleVector(3)
    libspice.mtxv_c(m1, vin, vout)
    return stypes.vectorToList(vout)


def mtxvg(m1, v2, ncol1, nr1r2):
    m1 = stypes.listtodoublematrix(m1, x=ncol1, y=nr1r2)
    v2 = stypes.toDoubleVector(v2)
    ncol1 = ctypes.c_int(ncol1)
    nr1r2 = ctypes.c_int(nr1r2)
    vout = stypes.doubleVector(ncol1.value)
    libspice.mtxvg_c(m1, v2, ncol1, nr1r2, vout)
    return stypes.vectorToList(vout)


def mxm(m1, m2):
    m1 = stypes.listtodoublematrix(m1)
    m2 = stypes.listtodoublematrix(m2)
    mout = stypes.doubleMatrix()
    libspice.mxm_c(m1, m2, mout)
    return stypes.matrixToList(mout)


def mxmg(m1, m2, nrow1, ncol1, ncol2):
    m1 = stypes.listtodoublematrix(m1, x=ncol1, y=nrow1)
    m2 = stypes.listtodoublematrix(m2, x=ncol2, y=ncol1)
    mout = stypes.doubleMatrix(x=ncol2, y=nrow1)
    nrow1 = ctypes.c_int(nrow1)
    ncol1 = ctypes.c_int(ncol1)
    ncol2 = ctypes.c_int(ncol2)
    libspice.mxmg_c(m1, m2, nrow1, ncol1, ncol2, mout)
    return stypes.matrixToList(mout)


def mxmt(m1, m2):
    m1 = stypes.listtodoublematrix(m1)
    m2 = stypes.listtodoublematrix(m2)
    mout = stypes.doubleMatrix()
    libspice.mxmt_c(m1, m2, mout)
    return stypes.matrixToList(mout)


def mxmtg(m1, m2, nrow1, nc1c2, nrow2):
    m1 = stypes.listtodoublematrix(m1, x=nc1c2, y=nrow1)
    m2 = stypes.listtodoublematrix(m2, x=nc1c2, y=nrow2)
    mout = stypes.doubleMatrix(x=nrow2, y=nrow1)
    nrow1 = ctypes.c_int(nrow1)
    nc1c2 = ctypes.c_int(nc1c2)
    nrow2 = ctypes.c_int(nrow2)
    libspice.mxmtg_c(m1, m2, nrow1, nc1c2, nrow2, mout)
    return stypes.matrixToList(mout)


def mxv(m1, vin):
    #Todo: test mxv
    m1 = stypes.listtodoublematrix(m1)
    vin = stypes.toDoubleVector(vin)
    vout = stypes.doubleVector(3)
    libspice.mxv_c(m1, vin, vout)
    return stypes.vectorToList(vout)


def mxvg(m1, v2, nrow1, nc1r2):
    m1 = stypes.listtodoublematrix(m1, x=nc1r2, y=nrow1)
    v2 = stypes.toDoubleVector(v2)
    nrow1 = ctypes.c_int(nrow1)
    nc1r2 = ctypes.c_int(nc1r2)
    vout = stypes.doubleVector(nrow1.value)
    libspice.mxvg_c(m1, v2, nrow1, nc1r2, vout)
    return stypes.vectorToList(vout)

########################################################################################################################
# N


def namfrm(frname):
    #todo: test namfrm
    frname = stypes.strtocharpoint(frname)
    frcode = ctypes.c_int()
    libspice.namfrm_c(frname, ctypes.byref(frcode))
    return frcode.value


def ncpos(string, chars, start):
    #todo: test ncpos
    string = stypes.strtocharpoint(string)
    chars = stypes.strtocharpoint(chars)
    start = ctypes.c_int(start)
    return libspice.ncpos_c(string, chars, start)


def ncposr(string, chars, start):
    #todo: test ncposr
    string = stypes.strtocharpoint(string)
    chars = stypes.strtocharpoint(chars)
    start = ctypes.c_int(start)
    return libspice.ncposr_c(string, chars, start)


def nearpt(positn, a, b, c):
    #Todo: test nearpt
    positn = stypes.toDoubleVector(positn)
    a = ctypes.c_double(a)
    b = ctypes.c_double(b)
    c = ctypes.c_double(c)
    npoint = stypes.doubleVector(3)
    alt = ctypes.c_double()
    libspice.nearpt_c(positn, a, b, c, npoint, ctypes.byref(alt))
    return stypes.vectorToList(npoint), alt.value


def npedln(a, b, c, linept, linedr):
    a = ctypes.c_double(a)
    b = ctypes.c_double(b)
    c = ctypes.c_double(c)
    linept = stypes.toDoubleVector(linept)
    linedr = stypes.toDoubleVector(linedr)
    pnear = stypes.doubleVector(3)
    dist = ctypes.c_double()
    libspice.npedln_c(a, b, c, linept, linedr, pnear, ctypes.byref(dist))
    return pnear, dist


def npelpt(point, ellips):
    #Todo: test npelpt
    assert(isinstance(ellips, stypes.Ellipse))
    point = stypes.toDoubleVector(point)
    pnear = stypes.doubleVector(3)
    dist = ctypes.c_double()
    libspice.npelpt_c(point, ctypes.byref(ellips), pnear, ctypes.byref(dist))


def nplnpt(linpt, lindir, point):
    linpt = stypes.toDoubleVector(linpt)
    lindir = stypes.toDoubleVector(lindir)
    point = stypes.toDoubleVector(point)
    pnear = stypes.doubleVector(3)
    dist = ctypes.c_double()
    libspice.nplnpt_c(linpt, lindir, point, pnear, ctypes.byref(dist))
    return stypes.toDoubleVector(pnear), dist.value


def nvc2pl(normal, constant):
    plane = stypes.Plane()
    normal = stypes.toDoubleVector(normal)
    constant = ctypes.c_double(constant)
    libspice.nvc2pl_c(normal, constant, ctypes.byref(plane))
    return plane


def nvp2pl(normal, point):
    #todo: test nvp2pl
    normal = stypes.toDoubleVector(normal)
    point = stypes.toDoubleVector(point)
    plane = stypes.Plane()
    libspice.nvp2pl_c(normal, point, ctypes.byref(plane))


########################################################################################################################
# O

def ordc(item, inset):
    #Todo: test ordc
    assert isinstance(inset, stypes.SpiceCell)
    assert inset.is_char()
    assert isinstance(item, str)
    item = stypes.strtocharpoint(item)
    return libspice.ordc_c(item, ctypes.byref(inset))


def ordd(item, inset):
    #Todo: test ordd
    assert isinstance(inset, stypes.SpiceCell)
    assert inset.is_double()
    item = ctypes.c_double(item)
    return libspice.ordd_c(item, ctypes.byref(inset))


def ordi(item, inset):
    #Todo: test ordi
    assert isinstance(inset, stypes.SpiceCell)
    assert inset.is_int()
    assert isinstance(item, int)
    item = ctypes.c_int(item)
    return libspice.ordi_c(item, ctypes.byref(inset))


def orderc(lenvals, array, ndim):
    #Todo: test, works but I am not convinced yet
    iorder = stypes.toIntVector([0] * ndim)
    ndim = ctypes.c_int(ndim)
    array = stypes.listtocharvector(array)
    lenvals = ctypes.c_int(lenvals)
    libspice.orderc_c(lenvals, array, ndim, iorder)
    return stypes.vectorToList(iorder)


def orderd(array, ndim):
    #Todo: test orderd
    array = stypes.toDoubleVector(array)
    iorder = stypes.toIntVector([0] * ndim)
    ndim = ctypes.c_int(ndim)
    libspice.orderd_c(array, ndim, iorder)
    return stypes.vectorToList(iorder)


def orderi(array, ndim):
    array = stypes.toIntVector(array)
    iorder = stypes.toIntVector([0] * ndim)
    ndim = ctypes.c_int(ndim)
    libspice.orderi_c(array, ndim, iorder)
    return stypes.vectorToList(iorder)


def oscelt(stat, et, mu):
    #Todo: Test oscelt
    stat = stypes.toDoubleVector(stat)
    et = ctypes.c_double(et)
    mu = ctypes.c_double(mu)
    elts = stypes.doubleVector(8)
    libspice.oscelt_c(stat, et, mu, elts)
    return stypes.vectorToList(elts)

########################################################################################################################
# P


def pckcov(pck, idcode, cover):
    pck = stypes.strtocharpoint(pck)
    idcode = ctypes.c_int(idcode)
    if not cover:
        cover = stypes.SPICEDOUBLE_CELL(2000)  # random size really
    assert isinstance(cover, stypes.SpiceCell)
    assert cover.dtype == 1
    libspice.pckcov_c(pck, idcode, ctypes.byref(cover))
    return cover


def pckfrm(pck, ids=None):
    #Todo: test pckfrm
    pck = stypes.strtocharpoint(pck)
    if not ids:
        ids = stypes.SPICEINT_CELL(1000)  # just picked 1000 for no reason
    assert isinstance(ids, stypes.SpiceCell)
    assert ids.dtype == 2
    libspice.pckfrm_c(pck, ctypes.byref(ids))
    return ids


def pcklof(filename):
    #Todo: test pcklof
    filename = stypes.strtocharpoint(filename)
    handle = ctypes.c_int()
    libspice.pcklof_c(filename, ctypes.byref(handle))
    return handle.value


def pckuof(handle):
    #Todo: test pckuof
    handle = ctypes.c_int(handle)
    libspice.pckuof_c(handle)
    pass


def pcpool(name, n, lenvals, cvals):
    #Todo: test pcpool
    name = stypes.strtocharpoint(name)
    cvals = stypes.listtocharvector(cvals)
    n = ctypes.c_int(n)
    lenvals = ctypes.c_int(lenvals)
    libspice.pcpool_c(name, n, lenvals, cvals)


def pdpool(name, n, dvals):
    #Todo: test pdpool
    name = stypes.strtocharpoint(name)
    dvals = stypes.toDoubleVector(dvals)
    n = ctypes.c_int(n)
    libspice.pdpool_c(name, n, dvals)


def pgrrec(body, lon, lat, alt, re, f):
    #Todo: test pgrrec
    body = stypes.strtocharpoint(body)
    lon = ctypes.c_double(lon)
    lat = ctypes.c_double(lat)
    alt = ctypes.c_double(alt)
    re = ctypes.c_double(re)
    f = ctypes.c_double(f)
    rectan = stypes.doubleVector(3)
    libspice.pgrrec(body, lon, lat, alt, re, f, rectan)
    return stypes.vectorToList(rectan)


def pi():
    return libspice.pi_c()


def pipool(name, n, ivals):
    #Todo: test pipool
    name = stypes.strtocharpoint(name)
    ivals = stypes.toIntVector(ivals)
    n = ctypes.c_int(n)
    libspice.pipool_c(name, n, ivals)


def pjelpl(elin, plane):
    #Todo: test pjelpl, figure out if we want asserts to help users
    assert(isinstance(elin, stypes.Ellipse))
    assert(isinstance(plane, stypes.Plane))
    elout = stypes.Ellipse()
    libspice.pjelpl_c(ctypes.byref(elin), ctypes.byref(plane), ctypes.byref(elout))


def pl2nvc(plane):
    #Works! we have working planes!
    assert(isinstance(plane, stypes.Plane))
    normal = stypes.doubleVector(3)
    constant = ctypes.c_double()
    libspice.pl2nvc_c(ctypes.byref(plane), normal, ctypes.byref(constant))
    return stypes.vectorToList(normal), constant.value


def pl2nvp(plane):
    #Todo: test pl2nvp
    assert(isinstance(plane, stypes.Plane))
    normal = stypes.doubleVector(3)
    point = stypes.doubleVector(3)
    libspice.pl2nvp_c(ctypes.byref(plane), normal, point)
    return stypes.vectorToList(normal), stypes.vectorToList(point)


def pl2psv(plane):
    #Todo: test pl2psv
    assert (isinstance(plane, stypes.Plane))
    point = stypes.doubleVector(3)
    span1 = stypes.doubleVector(3)
    span2 = stypes.doubleVector(3)
    libspice.pl2psv_c(ctypes.byref(plane), point, span1, span2)
    return stypes.vectorToList(point), stypes.vectorToList(span1), stypes.vectorToList(span2)


def pos(string, substr, start):
    string = stypes.strtocharpoint(string)
    substr = stypes.strtocharpoint(substr)
    start = ctypes.c_int(start)
    return libspice.pos_c(string, substr, start)


def posr(string, substr, start):
    string = stypes.strtocharpoint(string)
    substr = stypes.strtocharpoint(substr)
    start = ctypes.c_int(start)
    return libspice.posr_c(string, substr, start)


#prompt, skip for no as this is not really an important function for python users


def prop2b(gm, pvinit, dt):
    #todo: test prob2b
    gm = ctypes.c_double(gm)
    pvinit = stypes.toDoubleVector(pvinit)
    dt = ctypes.c_double(dt)
    pvprop = stypes.doubleVector(6)
    libspice.prop2b_c(gm, pvinit, dt, pvprop)
    return stypes.vectorToList(pvprop)


def prsdp(string):
    #Todo: test prsdp
    string = stypes.strtocharpoint(string)
    dpval = ctypes.c_double()
    libspice.prsdp_c(string, ctypes.byref(dpval))
    return dpval.value


def prsint(string):
    #Todo: test prsint
    string = stypes.strtocharpoint(string)
    intval = ctypes.c_int()
    libspice.prsint_c(string, ctypes.byref(intval))
    return intval.value


def psv2pl(point, span1, span2):
    #Todo: test psv2pl
    point = stypes.toDoubleVector(point)
    span1 = stypes.toDoubleVector(span1)
    span2 = stypes.toDoubleVector(span2)
    plane = stypes.Plane()
    libspice.psv2pl_c(point, span1, span2, ctypes.byref(plane))
    return plane


# skip putcml, is this really needed for python users?


def pxform(fromstr, tostr, et):
    #Todo: test pxform
    et = ctypes.c_double(et)
    tostr = stypes.strtocharpoint(tostr)
    fromstr = stypes.strtocharpoint(fromstr)
    rotatematrix = stypes.doubleMatrix()
    libspice.pxform_c(fromstr, tostr, et, rotatematrix)
    return stypes.matrixToList(rotatematrix)


########################################################################################################################
# Q


def q2m(q):
    q = stypes.toDoubleVector(q)
    mout = stypes.doubleMatrix()
    libspice.q2m_c(q, mout)
    return stypes.matrixToList(mout)


def qdq2av(q, dq):
    #Todo: test qdq2av
    q = stypes.toDoubleVector(q)
    dq = stypes.toDoubleVector(dq)
    vout = stypes.doubleVector(3)
    libspice.qdq2av(q, dq, vout)
    return stypes.vectorToList(vout)


def qxq(q1, q2):
    #Todo: test qxq
    q1 = stypes.toDoubleVector(q1)
    q2 = stypes.toDoubleVector(q2)
    vout = stypes.doubleVector(4)
    libspice.qxq_c(q1, q2, vout)
    return stypes.vectorToList(vout)

########################################################################################################################
# R


def radrec(inrange, re, dec):
    #Todo: test radrec
    inrange = ctypes.c_double(inrange)
    re = ctypes.c_double(re)
    dec = ctypes.c_double(dec)
    rectan = stypes.doubleVector(3)
    libspice.radrec_c(inrange, re, dec, rectan)
    return stypes.vectorToList(rectan)


def rav2xf(rot, av):
    #Todo: test rav2xf
    rot = stypes.listtodoublematrix(rot)
    av = stypes.toDoubleVector(av)
    xform = stypes.doubleMatrix(x=6, y=6)
    libspice.rav2xf_c(rot, av, xform)
    return stypes.matrixToList(xform)


def raxisa(matrix):
    #Todo: test raxisa
    matrix = stypes.listtodoublematrix(matrix)
    axis = stypes.doubleVector(3)
    angle = ctypes.c_double()
    libspice.raxisa_c(matrix, axis, ctypes.byref(angle))
    return stypes.vectorToList(axis), angle.value


def rdtext(file, lenout):
    #Todo: test rdtext
    file = stypes.strtocharpoint(file)
    line = stypes.strtocharpoint(" "*lenout)
    lenout = ctypes.c_int(lenout)
    eof = ctypes.c_bool()
    libspice.rdtext_c(file, lenout, line, ctypes.byref(eof))
    return line, eof.value


def reccyl(rectan):
    rectan = stypes.toDoubleVector(rectan)
    radius = ctypes.c_double(0)
    lon = ctypes.c_double(0)
    z = ctypes.c_double(0)
    libspice.reccyl_c(rectan, ctypes.byref(radius), ctypes.byref(lon), ctypes.byref(z))
    return radius.value, lon.value, z.value


def reclat(rectan):
    rectan = stypes.toDoubleVector(rectan)
    radius = ctypes.c_double(0)
    longitude = ctypes.c_double(0)
    latitude = ctypes.c_double(0)
    libspice.reclat_c(rectan, ctypes.byref(radius), ctypes.byref(longitude), ctypes.byref(latitude))
    return radius.value, longitude.value, latitude.value


def recgeo(rectan, re, f):
    rectan = stypes.toDoubleVector(rectan)
    re = ctypes.c_double(re)
    f = ctypes.c_double(f)
    longitude = ctypes.c_double(0)
    latitude = ctypes.c_double(0)
    alt = ctypes.c_double(0)
    libspice.recgeo_c(rectan, re, f, ctypes.byref(longitude), ctypes.byref(latitude), ctypes.byref(alt))
    return longitude.value, latitude.value, alt.value


def recpgr(body, rectan, re, f):
    #Todo: Test recpgr
    body = stypes.strtocharpoint(body)
    rectan = stypes.toDoubleVector(rectan)
    re = ctypes.c_double(re)
    f = ctypes.c_double(f)
    lon = ctypes.c_double()
    lat = ctypes.c_double()
    alt = ctypes.c_double()
    libspice.recpgr_c(body, rectan, re, f, ctypes.byref(lon), ctypes.byref(lat), ctypes.byref(alt))
    return lon.value, lat.value, alt.value


def recrad(rectan):
    #Todo: Test recrad
    rectan = stypes.toDoubleVector(rectan)
    outrange = ctypes.c_double()
    ra = ctypes.c_double()
    dec = ctypes.c_double()
    libspice.recrad_c(rectan, ctypes.byref(outrange), ctypes.byref(ra), ctypes.byref(dec))
    return outrange.value, ra.value, dec.value


def recsph(rectan):
    rectan = stypes.toDoubleVector(rectan)
    r = ctypes.c_double()
    colat = ctypes.c_double()
    lon = ctypes.c_double()
    libspice.recsph_c(rectan, ctypes.byref(r), ctypes.byref(colat), ctypes.byref(lon))
    return r.value, colat.value, lon.value


def removc(item, inset):
    #Todo: test removc
    assert isinstance(inset, stypes.SpiceCell)
    item = stypes.strtocharpoint(item)
    libspice.removc_c(item, ctypes.byref(inset))
    pass


def removd(item, inset):
    #Todo: test removd
    assert isinstance(inset, stypes.SpiceCell)
    item = ctypes.c_double(item)
    libspice.removd_c(item, ctypes.byref(inset))
    pass


def removi(item, inset):
    #Todo: test removi
    assert isinstance(inset, stypes.SpiceCell)
    item = ctypes.c_int(item)
    libspice.removi(item, ctypes.byref(inset))
    pass


def reordc(iorder, ndim, lenvals, array):
    #Todo: fix reordc, this should work, not sure why as shellc works despite this
    iorder = stypes.toIntVector(iorder)
    array = stypes.listToCharArray(array, xLen=lenvals, yLen=ndim)
    ndim = ctypes.c_int(ndim)
    lenvals = ctypes.c_int(lenvals)
    libspice.reordc_c(iorder, ndim, lenvals, array)
    return stypes.vectorToList(array)


def reordd(iorder, ndim, array):
    #todo: test reordd
    iorder = stypes.toIntVector(iorder)
    ndim = ctypes.c_int(ndim)
    array = stypes.toDoubleVector(array)
    libspice.reordd_c(iorder, ndim, array)
    return stypes.vectorToList(array)


def reordi(iorder, ndim, array):
    #Todo: test reordi
    iorder = stypes.toIntVector(iorder)
    ndim = ctypes.c_int(ndim)
    array = stypes.toIntVector(array)
    libspice.reordi_c(iorder, ndim, array)
    return stypes.vectorToList(array)


def reordl(iorder, ndim, array):
    #Todo: test reordl, not updating values
    iorder = stypes.toIntVector(iorder)
    ndim = ctypes.c_int(ndim)
    array = stypes.toBoolVector(array)
    libspice.reordl_c(iorder, ndim, array)
    return stypes.vectorToList(array)


def repmc(instr, marker, value, lenout):
    #Todo: test repmc
    instr = stypes.strtocharpoint(instr)
    marker = stypes.strtocharpoint(marker)
    value = stypes.strtocharpoint(value)
    lenout = ctypes.c_int(lenout)
    out = stypes.strtocharpoint(lenout)
    libspice.repmc_c(instr, marker, value, lenout, out)
    return out.value


def repmct(instr, marker, value, repcase, lenout):
    #Todo: test repmct
    instr = stypes.strtocharpoint(instr)
    marker = stypes.strtocharpoint(marker)
    value = ctypes.c_double(value)
    repcase = ctypes.c_char(repcase)
    lenout = ctypes.c_int(lenout)
    out = stypes.strtocharpoint(lenout)
    libspice.repmct_c(instr, marker, value, repcase, lenout, out)
    return out.value


def repmd(instr, marker, value, sigdig, lenout):
    #Todo: test repmd
    instr = stypes.strtocharpoint(instr)
    marker = stypes.strtocharpoint(marker)
    value = ctypes.c_double(value)
    sigdig = ctypes.c_int(sigdig)
    lenout = ctypes.c_int(lenout)
    out = stypes.strtocharpoint(lenout)
    libspice.repmd_c(instr, marker, value, sigdig, lenout, out)
    return out.value


def repmf(instr, marker, value, sigdig, informat, lenout):
    #Todo: test repmf
    instr = stypes.strtocharpoint(instr)
    marker = stypes.strtocharpoint(marker)
    value = ctypes.c_double(value)
    sigdig = ctypes.c_int(sigdig)
    lenout = ctypes.c_int(lenout)
    informat = ctypes.c_char(informat)
    out = stypes.strtocharpoint(lenout)
    libspice.repmf(instr, marker, value, sigdig, informat, lenout, out)
    return out.value


def repmi(instr, marker, value, lenout):
    #Todo: test repmi
    instr = stypes.strtocharpoint(instr)
    marker = stypes.strtocharpoint(marker)
    value = ctypes.c_int(value)
    lenout = ctypes.c_int(lenout)
    out = stypes.strtocharpoint(lenout)
    libspice.repmi_c(instr, marker, value, lenout, out)
    return out.value


def repmot(instr, marker, value, repcase, lenout):
    #Todo: test repmot
    instr = stypes.strtocharpoint(instr)
    marker = stypes.strtocharpoint(marker)
    value = ctypes.c_int(value)
    repcase = ctypes.c_char(repcase)
    lenout = ctypes.c_int(lenout)
    out = stypes.strtocharpoint(lenout)
    libspice.repmot_c(instr, marker, value, repcase, lenout, out)
    return out.value


def reset():
    libspice.reset_c()
    pass


def return_c():
    #Todo: test return_c
    return libspice.return_c()


def rotate(angle, iaxis):
    #Todo: test rotate
    angle = ctypes.c_double(angle)
    iaxis = ctypes.c_int(iaxis)
    mout = stypes.doubleMatrix()
    libspice.rotate_c(angle, iaxis, mout)
    return stypes.matrixToList(mout)


def rotmat(m1, angle, iaxis):
    #Todo: test rotmat
    m1 = stypes.listtodoublematrix(m1)
    angle = ctypes.c_double(angle)
    iaxis = ctypes.c_int(iaxis)
    mout = stypes.doubleMatrix()
    libspice.rotmat_c(m1, angle, iaxis, mout)
    return stypes.matrixToList(mout)


def rotvec(v1, angle, iaxis):
    #Todo: test rotvec
    v1 = stypes.toDoubleVector(v1)
    angle = ctypes.c_double(angle)
    iaxis = ctypes.c_int(iaxis)
    vout = stypes.doubleVector(3)
    libspice.rotvec_c(v1, angle, iaxis, vout)
    return stypes.vectorToList(vout)


def rpd():
    return libspice.rpd_c()


def rquad(a, b, c):
    a = ctypes.c_double(a)
    b = ctypes.c_double(b)
    c = ctypes.c_double(c)
    root1 = stypes.doubleVector(2)
    root2 = stypes.doubleVector(2)
    libspice.rquad(a, b, c, root1, root2)
    return root1, root2

########################################################################################################################
# S


def saelgv(vec1, vec2):
    #Todo: test saelgv
    vec1 = stypes.toDoubleVector(vec1)
    vec2 = stypes.toDoubleVector(vec2)
    smajor = stypes.doubleVector(3)
    sminor = stypes.doubleVector(3)
    libspice.saelgv_c(vec1, vec2, smajor, sminor)
    return stypes.vectorToList(smajor), stypes.vectorToList(sminor)


def scard(incard, cell):
    #Todo: test scard
    assert isinstance(cell, stypes.SpiceCell)
    incard = ctypes.c_int(incard)
    libspice.scard_c(incard, ctypes.byref(cell))
    return cell


def scdecd(sc, sclkdp, lenout, MXPART=None):
    #todo: figure out how to use mxpart, and test scdecd
    sc = ctypes.c_int(sc)
    sclkdp = ctypes.c_double(sclkdp)
    sclkch = stypes.strtocharpoint(" "*lenout)
    lenout = ctypes.c_int(lenout)
    libspice.scdecd_c(sc, sclkdp, lenout, sclkch)
    return sclkch


def sce2c(sc, et):
    #todo: test sce2c
    sc = ctypes.c_int(sc)
    et = ctypes.c_double(et)
    sclkdp = ctypes.c_double()
    libspice.sce2c_c(sc, et, ctypes.byref(sclkdp))
    return sclkdp.value


def sce2s(sc, et, lenout):
    #todo: test sce2s
    sc = ctypes.c_int(sc)
    et = ctypes.c_double(et)
    sclkch = stypes.strtocharpoint(" " * lenout)
    lenout = ctypes.c_int(lenout)
    libspice.sce2s_c(sc, et, lenout, sclkch)
    return sclkch


def sce2t(sc, et):
    #todo; test sce2t
    sc = ctypes.c_int(sc)
    et = ctypes.c_double(et)
    sclkdp = ctypes.c_double()
    libspice.sce2t_c(sc, et, ctypes.byref(sclkdp))
    return sclkdp.value


def scencd(sc, sclkch, MXPART=None):
    #todo: figure out how to use mxpart, and test scencd
    sc = ctypes.c_int(sc)
    sclkch = stypes.strtocharpoint(sclkch)
    sclkdp = ctypes.c_double()
    libspice.scencd_c(sc, sclkch, ctypes.byref(sclkdp))
    return sclkdp.value


def scfmt(sc, ticks, lenout):
    #Todo: test scfmt
    sc = ctypes.c_int(sc)
    ticks = ctypes.c_double(ticks)
    clkstr = stypes.strtocharpoint(lenout)
    lenout = ctypes.c_int(lenout)
    libspice.scfmt_c(sc, ticks, lenout, clkstr)
    return clkstr


def scpart(sc, nparts, pstart, MXPART=None):
    #todo: figure out how to use mxpart, and test scpart
    sc = ctypes.c_int(sc)
    nparts = ctypes.c_int(nparts)
    pstart = ctypes.c_double(pstart)
    pstop = ctypes.c_double()
    libspice.scpart_c(sc, nparts, pstart, ctypes.byref(pstop))
    return pstop.value


def scs2e(sc, sclkch):
    #todo: test scs2e
    sc = ctypes.c_int(sc)
    sclkch = stypes.strtocharpoint(sclkch)
    et = ctypes.c_double()
    libspice.scs2e_c(sc, sclkch, ctypes.byref(et))
    return et.value


def sct2e(sc, sclkdp):
    #todo: test scs2e
    sc = ctypes.c_int(sc)
    sclkdp = ctypes.c_double(sclkdp)
    et = ctypes.c_double()
    libspice.sct2e_c(sc, sclkdp, ctypes.byref(et))
    return et.value


def sctiks(sc, clkstr):
    #todo: test sctiks
    sc = ctypes.c_int(sc)
    clkstr = stypes.strtocharpoint(clkstr)
    ticks = ctypes.c_double()
    libspice.sctiks_c(sc, clkstr, ctypes.byref(ticks))
    return ticks.value


def sdiff(a, b):
    #Todo: test sdiff
    assert isinstance(a, stypes.SpiceCell)
    assert isinstance(b, stypes.SpiceCell)
    assert a.dtype == b.dtype
    assert a.dtype == 0 or a.dtype == 1 or a.dtype == 2
    if a.dtype is 0:
        c = stypes.SPICECHAR_CELL(a.size, a.length)
    if a.dtype is 1:
        c = stypes.SPICEDOUBLE_CELL(a.size)
    elif a.dtype is 2:
        c = stypes.SPICEINT_CELL(a.size)
    else:
        raise NotImplementedError
    libspice.sdiff_c(ctypes.byref(a), ctypes.byref(b), ctypes.byref(c))
    return c


def set(a, op, b):
    #Todo: test set
    assert isinstance(a, stypes.SpiceCell)
    assert isinstance(b, stypes.SpiceCell)
    assert a.dtype == b.dtype
    assert isinstance(op, str)
    op = stypes.strtocharpoint(op)
    return libspice.set_c(ctypes.byref(a), op, ctypes.byref(b))


def setmsg(message):
    #todo: test setmsg
    message = stypes.strtocharpoint(message)
    libspice.setmsg_c(message)
    pass


def shellc(ndim, lenvals, array):
    #This works! looks like this is a mutable 2d char array
    array = stypes.listToCharArray(array, xLen=lenvals, yLen=ndim)
    ndim = ctypes.c_int(ndim)
    lenvals = ctypes.c_int(lenvals)
    libspice.shellc_c(ndim, lenvals, ctypes.byref(array))
    return stypes.vectorToList(array)


def shelld(ndim, array):
    #Todo: Works!, use this as example for "I/O" parameters
    array = stypes.toDoubleVector(array)
    ndim = ctypes.c_int(ndim)
    libspice.shelld_c(ndim, ctypes.cast(array, ctypes.POINTER(ctypes.c_double)))
    return stypes.vectorToList(array)


def shelli(ndim, array):
    #Todo: Works!, use this as example for "I/O" parameters
    array = stypes.toIntVector(array)
    ndim = ctypes.c_int(ndim)
    libspice.shelli_c(ndim, ctypes.cast(array, ctypes.POINTER(ctypes.c_int)))
    return stypes.vectorToList(array)


def sigerr(message):
    #todo: test
    message = stypes.strtocharpoint(message)
    libspice.sigerr_c(message)
    pass


def sincpt(method, target, et, fixref, abcorr, obsrvr, dref, dvec):
    method = stypes.strtocharpoint(method)
    target = stypes.strtocharpoint(target)
    et = ctypes.c_double(et)
    fixref = stypes.strtocharpoint(fixref)
    abcorr = stypes.strtocharpoint(abcorr)
    obsrvr = stypes.strtocharpoint(obsrvr)
    dref = stypes.strtocharpoint(dref)
    dvec = stypes.toDoubleVector(dvec)
    spoint = stypes.doubleVector(3)
    trgepc = ctypes.c_double(0)
    srfvec = stypes.doubleVector(3)
    found = ctypes.c_bool(0)
    libspice.sincpt_c(method, target, et, fixref, abcorr, obsrvr, dref, dvec, spoint, ctypes.byref(trgepc), srfvec, ctypes.byref(found))
    return stypes.vectorToList(spoint), trgepc.value, stypes.vectorToList(srfvec), found.value


def size(cell):
    #Todo: test size
    assert isinstance(cell, stypes.SpiceCell)
    return libspice.size_c(ctypes.byref(cell))


def spd():
    return libspice.spd_c()


def sphcyl(radius, colat, slon):
    radius = ctypes.c_double(radius)
    colat = ctypes.c_double(colat)
    slon = ctypes.c_double(slon)
    r = ctypes.c_double()
    lon = ctypes.c_double()
    z = ctypes.c_double()
    libspice.sphcyl_c(radius, colat, slon, ctypes.byref(r), ctypes.byref(lon), ctypes.byref(z))
    return r.value, lon.value, z.value


def sphlat(r, colat, lons):
    r = ctypes.c_double(r)
    colat = ctypes.c_double(colat)
    lons = ctypes.c_double(lons)
    radius = ctypes.c_double()
    lon = ctypes.c_double()
    lat = ctypes.c_double()
    libspice.sphcyl_c(r, colat, lons, ctypes.byref(radius), ctypes.byref(lon), ctypes.byref(lat))
    return radius.value, lon.value, lat.value


def sphrec(r, colat, lon):
    r = ctypes.c_double(r)
    colat = ctypes.c_double(colat)
    lon = ctypes.c_double(lon)
    rectan = stypes.doubleVector(3)
    libspice.sphrec_c(r, colat, lon, rectan)
    return stypes.vectorToList(rectan)


def spkacs(targ, et, ref, abcorr, obs):
    #Todo: test spkacs
    targ = ctypes.c_int(targ)
    et = ctypes.c_int(et)
    ref = stypes.strtocharpoint(ref)
    abcorr = stypes.strtocharpoint(abcorr)
    obs = ctypes.c_int(obs)
    starg = stypes.doubleVector(6)
    lt = ctypes.c_double()
    dlt = ctypes.c_double()
    libspice.spkacs_c(targ, et, ref, abcorr, obs, starg, ctypes.byref(lt), ctypes.byref(dlt))
    return stypes.vectorToList(starg), lt.value, dlt.value


def spkapo(targ, et, ref, sobs, abcorr):
    #Todo: test spkacs
    targ = ctypes.c_int(targ)
    et = ctypes.c_int(et)
    ref = stypes.strtocharpoint(ref)
    abcorr = stypes.strtocharpoint(abcorr)
    sobs = stypes.toDoubleVector(sobs)
    ptarg = stypes.doubleVector(3)
    lt = ctypes.c_double()
    libspice.spkapo_c(targ, et, ref, sobs, abcorr, ptarg, ctypes.byref(lt))
    return stypes.vectorToList(ptarg), lt.value


def spkapp(targ, et, ref, sobs, abcorr):
    #Todo: test spkapp (depricated)
    targ = ctypes.c_int(targ)
    et = ctypes.c_int(et)
    ref = stypes.strtocharpoint(ref)
    abcorr = stypes.strtocharpoint(abcorr)
    sobs = stypes.toDoubleVector(sobs)
    starg = stypes.doubleVector(6)
    lt = ctypes.c_double()
    libspice.spkapp_c(targ, et, ref, sobs, abcorr, starg, ctypes.byref(lt))
    return stypes.vectorToList(starg), lt.value


def spkaps(targ, et, ref, abcorr, stobs, accobs):
    #Todo: test spkaps
    targ = ctypes.c_int(targ)
    et = ctypes.c_int(et)
    ref = stypes.strtocharpoint(ref)
    abcorr = stypes.strtocharpoint(abcorr)
    stobs = stypes.toDoubleVector(stobs)
    accobs = stypes.toDoubleVector(accobs)
    starg = stypes.doubleVector(6)
    lt = ctypes.c_double()
    dlt = ctypes.c_double()
    libspice.spkaps_c(targ, et, ref, abcorr, stobs, accobs, starg, ctypes.byref(lt), ctypes.byref(dlt))
    return stypes.vectorToList(starg), lt.value, dlt.value


def spk14a(handle, ncsets, coeffs, epochs):
    #Todo: test spk14a
    handle = ctypes.c_int(handle)
    ncsets = ctypes.c_int(ncsets)
    coeffs = stypes.toDoubleVector(coeffs)
    epochs = stypes.toDoubleVector(epochs)
    libspice.spk14a_c(handle, ncsets, ctypes.byref(coeffs), ctypes.byref(epochs))
    pass


def spk14b(handle, segid, body, center, framename, first, last, chbdeg):
    #Todo: test spk14b
    handle = ctypes.c_int(handle)
    segid = stypes.strtocharpoint(segid)
    body = ctypes.c_int(body)
    center = ctypes.c_int(center)
    framename = stypes.strtocharpoint(framename)
    first = ctypes.c_double(first)
    last = ctypes.c_double(last)
    chbdeg = ctypes.c_int(chbdeg)
    libspice.spk14b_c(handle, segid, body, center, framename, first, last, chbdeg)
    pass


def spk14e(handle):
    #Todo: test spk14e
    handle = ctypes.c_int(handle)
    libspice.spk14e_c(handle)
    pass


def spkcls(handle):
    #Todo: test spkcls
    handle = ctypes.c_int(handle)
    libspice.spkcls_c(handle)
    pass


def spkcov(spk, idcode, cover=None):
    #Todo: test spkcov
    spk = stypes.strtocharpoint(spk)
    idcode = ctypes.c_int(idcode)
    if not cover:
        cover = stypes.SPICEDOUBLE_CELL(2000)  #random size really
    assert isinstance(cover, stypes.SpiceCell)
    assert cover.dtype == 1
    libspice.spkcov_c(spk, idcode, ctypes.byref(cover))
    return cover


def spkez(targ, et, ref, abcorr, obs):
    #Todo: test spkez
    targ = ctypes.c_int(targ)
    et = ctypes.c_int(et)
    ref = stypes.strtocharpoint(ref)
    abcorr = stypes.strtocharpoint(abcorr)
    obs = ctypes.c_int(obs)
    starg = stypes.doubleVector(6)
    lt = ctypes.c_double()
    libspice.spkez_c(targ, et, ref, abcorr, obs, starg, ctypes.byref(lt))
    return stypes.vectorToList(starg), lt.value


def spkezp(targ, et, ref, abcorr, obs):
    #Todo: test spkezp
    targ = ctypes.c_int(targ)
    et = ctypes.c_int(et)
    ref = stypes.strtocharpoint(ref)
    abcorr = stypes.strtocharpoint(abcorr)
    obs = ctypes.c_int(obs)
    ptarg = stypes.doubleVector(3)
    lt = ctypes.c_double()
    libspice.spkezp_c(targ, et, ref, abcorr, obs, ptarg, ctypes.byref(lt))
    return stypes.vectorToList(ptarg), lt.value


def spkezr(targ, et, ref, abcorr, obs):
    #Todo: test spkezr
    targ = stypes.strtocharpoint(targ)
    et = ctypes.c_int(et)
    ref = stypes.strtocharpoint(ref)
    abcorr = stypes.strtocharpoint(abcorr)
    obs = ctypes.c_int(obs)
    starg = stypes.doubleVector(6)
    lt = ctypes.c_double()
    libspice.spkezr_c(targ, et, ref, abcorr, obs, starg, ctypes.byref(lt))
    return stypes.vectorToList(starg), lt.value


def spkgeo(targ, et, ref, obs):
    #Todo: test spkgeo
    targ = ctypes.c_int(targ)
    et = ctypes.c_int(et)
    ref = stypes.strtocharpoint(ref)
    obs = ctypes.c_int(obs)
    state = stypes.doubleVector(6)
    lt = ctypes.c_double()
    libspice.spkgeo_c(targ, et, ref, obs, state, ctypes.byref(lt))
    return stypes.vectorToList(state), lt.value


def spkgps(targ, et, ref, obs):
    #Todo: test spkgps
    targ = ctypes.c_int(targ)
    et = ctypes.c_int(et)
    ref = stypes.strtocharpoint(ref)
    obs = ctypes.c_int(obs)
    position = stypes.doubleVector(3)
    lt = ctypes.c_double()
    libspice.spkgeo_c(targ, et, ref, obs, position, ctypes.byref(lt))
    return stypes.vectorToList(position), lt.value


def spklef(filename):
    #Todo: test spklef
    filename = stypes.strtocharpoint(filename)
    handle = ctypes.c_int()
    libspice.spklef_c(filename, ctypes.byref(handle))
    return handle.value


def spkltc(targ, et, ref, abcorr, stobs):
    #Todo: test spkltc
    assert len(stobs) == 6
    targ = stypes.strtocharpoint(targ)
    et = ctypes.c_int(et)
    ref = stypes.strtocharpoint(ref)
    abcorr = stypes.strtocharpoint(abcorr)
    stobs = stypes.toDoubleVector(stobs)
    starg = stypes.doubleVector(6)
    lt = ctypes.c_double()
    dlt = ctypes.c_double()
    libspice.spkltc_c(targ, et, ref, abcorr, stobs, starg, ctypes.byref(lt), ctypes.byref(dlt))
    return stypes.vectorToList(starg), lt.value, dlt.value


def spkobj(spk, ids=None):
    #Todo: test spkobj
    spk = stypes.strtocharpoint(spk)
    if not ids:
        ids = stypes.SPICEINT_CELL(1000)  # just picked 1000 for no reason
    assert isinstance(ids, stypes.SpiceCell)
    assert ids.dtype == 2
    libspice.spkobj_c(spk, ctypes.byref(ids))
    return ids


def spkopa(filename):
    #Todo: test spkopa
    filename = stypes.strtocharpoint(filename)
    handle = ctypes.c_int()
    libspice.spkopa_c(filename, ctypes.byref(handle))
    return handle.value


def spkopn(filename, ifname, ncomch):
    #Todo: test spkopn
    filename = stypes.strtocharpoint(filename)
    ifname = stypes.strtocharpoint(ifname)
    ncomch = ctypes.c_int(ncomch)
    handle = ctypes.c_int()
    libspice.spkopn_c(filename, ifname, ncomch, ctypes.byref(handle))
    return handle.value


def spkpds(body, center, framestr, typenum, first, last):
    #Todo: test spkpds
    body = ctypes.c_int(body)
    center = ctypes.c_int(center)
    framestr = stypes.strtocharpoint(framestr)
    typenum = ctypes.c_int(typenum)
    first = ctypes.c_double(first)
    last = ctypes.c_double(last)
    descr = stypes.doubleVector(5)
    libspice.spkpds_c(body, center, framestr, typenum, first, last, descr)
    return stypes.vectorToList(descr)


def spkpos(targ, et, ref, abcorr, obs):
    if hasattr(et, "__iter__"):
        ptarg = []
        ltimes = []
        for time in et:
            temp_ptarg, temp_ltime = spkpos(targ, time, ref, abcorr, obs)
            ptarg.append(temp_ptarg)
            ltimes.append(temp_ltime)
        return ptarg, ltimes
    targ = stypes.strtocharpoint(targ)
    ref = stypes.strtocharpoint(ref)
    abcorr = stypes.strtocharpoint(abcorr)
    obs = stypes.strtocharpoint(obs)
    ptarg = stypes.doubleVector(3)
    lt = ctypes.c_double()
    libspice.spkpos_c(targ, et, ref, abcorr, obs, ptarg, ctypes.byref(lt))
    return stypes.vectorToList(ptarg), lt.value


def spkssb(targ, et, ref):
    #Todo: test spkssb
    targ = ctypes.c_int(targ)
    et = ctypes.c_double(et)
    ref = stypes.strtocharpoint(ref)
    starg = stypes.doubleVector(6)
    libspice.spkssb_c(targ, et, ref, starg)
    pass


def spksub(handle, descr, identin, begin, end, newh):
    #Todo: test spksub
    assert len(descr) is 5
    handle = ctypes.c_int(handle)
    descr = stypes.toDoubleVector(descr)
    identin = stypes.strtocharpoint(identin)
    begin = ctypes.c_int(begin)
    end = ctypes.c_int(end)
    newh = ctypes.c_int(newh)
    libspice.spksub_c(handle, descr, identin, begin, end, newh)
    pass


def spkuds(descr):
    #Todo: test spkuds
    assert len(descr) is 5
    descr = stypes.toDoubleVector(descr)
    body = ctypes.c_int()
    center = ctypes.c_int()
    framenum = ctypes.c_int()
    typenum = ctypes.c_int()
    first = ctypes.c_double()
    last = ctypes.c_double()
    begin = ctypes.c_int()
    end = ctypes.c_int()
    libspice.spkuds_c(descr, ctypes.byref(body), ctypes.byref(center), ctypes.byref(framenum), ctypes.byref(typenum), ctypes.byref(first), ctypes.byref(last), ctypes.byref(begin), ctypes.byref(end))
    return body.value, center.value, framenum.value, typenum.value, first.value, last.value, begin.value, end.value


def spkuef(handle):
    #Todo: test spkuef
    handle = ctypes.c_int(handle)
    libspice.spkuef_c(handle)
    pass


def spkw02(handle, body, center, inframe, first, last, segid, intlen, n, polydg, cdata, btime):
    #Todo: test spkw02
    # array[] can be treated as array *,
    # http://stackoverflow.com/questions/5573310/difference-between-passing-array-and-array-pointer-into-function-in-c
    handle = ctypes.c_int(handle)
    body = ctypes.c_int(body)
    center = ctypes.c_int(center)
    inframe = stypes.strtocharpoint(inframe)
    first = ctypes.c_double(first)
    last = ctypes.c_double(last)
    segid = stypes.strtocharpoint(segid)
    intlen = ctypes.c_double(intlen)
    n = ctypes.c_int(n)
    polydg = ctypes.c_int(polydg)
    cdata = stypes.toDoubleVector(cdata)
    btime = ctypes.c_double(btime)
    libspice.spkw02_c(handle, body, center, inframe, first, last, segid, intlen, n, polydg, ctypes.byref(cdata), btime)
    pass


def spkw03(handle, body, center, inframe, first, last, segid, intlen, n, polydg, cdata, btime):
    #Todo: test spkw03
    # array[] can be treated as array *,
    # http://stackoverflow.com/questions/5573310/difference-between-passing-array-and-array-pointer-into-function-in-c
    handle = ctypes.c_int(handle)
    body = ctypes.c_int(body)
    center = ctypes.c_int(center)
    inframe = stypes.strtocharpoint(inframe)
    first = ctypes.c_double(first)
    last = ctypes.c_double(last)
    segid = stypes.strtocharpoint(segid)
    intlen = ctypes.c_double(intlen)
    n = ctypes.c_int(n)
    polydg = ctypes.c_int(polydg)
    cdata = stypes.toDoubleVector(cdata)
    btime = ctypes.c_double(btime)
    libspice.spkw03_c(handle, body, center, inframe, first, last, segid, intlen, n, polydg, ctypes.byref(cdata), btime)
    pass


def spkw05(handle, body, center, inframe, first, last, segid, gm, n, states, epochs):
    #Todo: test spkw05
    handle = ctypes.c_int(handle)
    body = ctypes.c_int(body)
    center = ctypes.c_int(center)
    inframe = stypes.strtocharpoint(inframe)
    first = ctypes.c_double(first)
    last = ctypes.c_double(last)
    segid = stypes.strtocharpoint(segid)
    gm = ctypes.c_int(gm)
    n = ctypes.c_int(n)
    states = stypes.toDoubleMatrix(states)  # X by 6 array
    epochs = stypes.toDoubleVector(epochs)
    libspice.spkw05_c(handle, body, center, inframe, first, last, segid, gm, n, ctypes.byref(states), ctypes.byref(epochs))
    pass


def spkw08(handle, body, center, inframe, first, last, segid, degree, n, states, epoch1, step):
    #Todo: test spkw08
    handle = ctypes.c_int(handle)
    body = ctypes.c_int(body)
    center = ctypes.c_int(center)
    inframe = stypes.strtocharpoint(inframe)
    first = ctypes.c_double(first)
    last = ctypes.c_double(last)
    segid = stypes.strtocharpoint(segid)
    degree = ctypes.c_int(degree)
    n = ctypes.c_int(n)
    states = stypes.toDoubleMatrix(states)  # X by 6 array
    epoch1 = ctypes.c_double(epoch1)
    step = ctypes.c_double(step)
    libspice.spkw08_c(handle, body, center, inframe, first, last, segid, degree, n, ctypes.byref(states), epoch1, step)
    pass


def spkw09(handle, body, center, inframe, first, last, segid, degree, n, states, epochs):
    #Todo: test spkw09
    handle = ctypes.c_int(handle)
    body = ctypes.c_int(body)
    center = ctypes.c_int(center)
    inframe = stypes.strtocharpoint(inframe)
    first = ctypes.c_double(first)
    last = ctypes.c_double(last)
    segid = stypes.strtocharpoint(segid)
    degree = ctypes.c_int(degree)
    n = ctypes.c_int(n)
    states = stypes.toDoubleMatrix(states)  # X by 6 array
    epochs = stypes.toDoubleMatrix(epochs)
    libspice.spkw09_c(handle, body, center, inframe, first, last, segid, degree, n, ctypes.byref(states), ctypes.byref(epochs))
    pass


def spkw10(handle, body, center, inframe, first, last, segid, consts, n, elems, epochs):
    #Todo: test spkw10
    handle = ctypes.c_int(handle)
    body = ctypes.c_int(body)
    center = ctypes.c_int(center)
    inframe = stypes.strtocharpoint(inframe)
    first = ctypes.c_double(first)
    last = ctypes.c_double(last)
    segid = stypes.strtocharpoint(segid)
    consts = stypes.toDoubleVector(consts)
    n = ctypes.c_int(n)
    elems = stypes.toDoubleVector(elems)
    epochs = stypes.toDoubleVector(epochs)
    libspice.spkw10_c(handle, body, center, inframe, first, last, segid, consts, n, ctypes.byref(elems), ctypes.byref(epochs))
    pass


def spkw12(handle, body, center, inframe, first, last, segid, degree, n, states, epoch0, step):
    #Todo: test spkw12
    handle = ctypes.c_int(handle)
    body = ctypes.c_int(body)
    center = ctypes.c_int(center)
    inframe = stypes.strtocharpoint(inframe)
    first = ctypes.c_double(first)
    last = ctypes.c_double(last)
    segid = stypes.strtocharpoint(segid)
    degree = ctypes.c_int(degree)
    n = ctypes.c_int(n)
    states = stypes.toDoubleMatrix(states)  # X by 6 array
    epoch0 = ctypes.c_double(epoch0)
    step = ctypes.c_double(step)
    libspice.spkw12_c(handle, body, center, inframe, first, last, segid, degree, n, ctypes.byref(states), epoch0, step)
    pass


def spkw13(handle, body, center, inframe, first, last, segid, degree, n, states, epochs):
    #Todo: test spkw13
    handle = ctypes.c_int(handle)
    body = ctypes.c_int(body)
    center = ctypes.c_int(center)
    inframe = stypes.strtocharpoint(inframe)
    first = ctypes.c_double(first)
    last = ctypes.c_double(last)
    segid = stypes.strtocharpoint(segid)
    degree = ctypes.c_int(degree)
    n = ctypes.c_int(n)
    states = stypes.toDoubleMatrix(states)  # X by 6 array
    epochs = stypes.toDoubleMatrix(epochs)
    libspice.spkw13_c(handle, body, center, inframe, first, last, segid, degree, n, ctypes.byref(states), ctypes.byref(epochs))
    pass


def spkw15(handle, body, center, inframe, first, last, segid, epoch, tp, pa, p, ecc, j2flg, pv, gm, j2, radius):
    #Todo: test spkw15
    handle = ctypes.c_int(handle)
    body = ctypes.c_int(body)
    center = ctypes.c_int(center)
    inframe = stypes.strtocharpoint(inframe)
    first = ctypes.c_double(first)
    last = ctypes.c_double(last)
    segid = stypes.strtocharpoint(segid)
    epoch = ctypes.c_double(epoch)
    tp = stypes.toDoubleVector(tp)
    pa = stypes.toDoubleVector(pa)
    p = ctypes.c_double(p)
    ecc = ctypes.c_double(ecc)
    j2flg = ctypes.c_double(j2flg)
    pv = ctypes.c_double(pv)
    gm = ctypes.c_double(gm)
    j2 = ctypes.c_double(j2)
    radius = ctypes.c_double(radius)
    libspice.spkw15_c(handle, body, center, inframe, first, last, segid, epoch, tp, pa, p, ecc, j2flg, pv, gm, j2, radius)
    pass


def spkw17(handle, body, center, inframe, first, last, segid, epoch, eqel, rapol, decpol):
    #Todo: test spkw17
    handle = ctypes.c_int(handle)
    body = ctypes.c_int(body)
    center = ctypes.c_int(center)
    inframe = stypes.strtocharpoint(inframe)
    first = ctypes.c_double(first)
    last = ctypes.c_double(last)
    segid = stypes.strtocharpoint(segid)
    epoch = ctypes.c_double(epoch)
    eqel = stypes.toDoubleVector(eqel)
    rapol = ctypes.c_double(rapol)
    decpol = ctypes.c_double(decpol)
    libspice.spkw17_c(handle, body, center, inframe, first, last, segid, epoch, eqel, rapol, decpol)
    pass


#spkw18


def srfrec(body, longitude, latitude):
    #Todo: test srfrec
    body = ctypes.c_int(body)
    longitude = ctypes.c_double(longitude)
    latitude = ctypes.c_double(latitude)
    rectan = stypes.doubleVector(3)
    libspice.srfrec_c(body, longitude, latitude, rectan)
    return stypes.vectorToList(rectan)


def srfxpt(method, target, et, abcorr, obsrvr, dref, dvec):
    #Todo: test srfxpt, but it is depricated
    method = stypes.strtocharpoint(method)
    target = stypes.strtocharpoint(target)
    et = ctypes.c_double(et)
    abcorr = stypes.strtocharpoint(abcorr)
    obsrvr = stypes.strtocharpoint(obsrvr)
    dref = stypes.strtocharpoint(dref)
    dvec = stypes.toDoubleVector(dvec)
    spoint = stypes.doubleVector(3)
    trgepc = ctypes.c_double()
    dist = ctypes.c_double()
    obspos = stypes.doubleVector(3)
    found = ctypes.c_bool()
    libspice.srfxpt_c(method, target, et, abcorr, obsrvr, dref, dvec,
                      spoint, ctypes.byref(dist), ctypes.byref(trgepc), obspos, ctypes.byref(found))
    return stypes.vectorToList(spoint), dist.value, trgepc.value, stypes.vectorToList(obspos), found.value


def ssize(newsize, cell):
    assert isinstance(cell, stypes.SpiceCell)
    newsize = ctypes.c_int(newsize)
    libspice.ssize_c(newsize, ctypes.byref(cell))
    return cell


def stelab(pobj, vobs):
    #Todo: test stelab
    pobj = stypes.toDoubleVector(pobj)
    vobs = stypes.toDoubleVector(vobs)
    appobj = stypes.doubleVector(3)
    libspice.stelab_c(pobj, vobs, appobj)
    return stypes.vectorToList(appobj)


def stpool(item, nth, contin, lenout):
    #Todo: test stpool
    item = stypes.strtocharpoint(item)
    contin = stypes.strtocharpoint(contin)
    nth = ctypes.c_int(nth)
    lenout = ctypes.c_int(lenout)
    strout = stypes.strtocharpoint(" "*lenout.value)
    found = ctypes.c_bool()
    size = ctypes.c_int()
    libspice.stpool_c(item, nth, contin, lenout, strout, ctypes.byref(size), ctypes.byref(found))
    return strout, size.value, found.value


def str2et(time):
    time = stypes.strtocharpoint(time)
    et = ctypes.c_double(0)
    libspice.str2et_c(time, ctypes.byref(et))
    return et.value


def subpnt(method, target, et, fixref, abcorr, obsrvr):
    #Todo: test subpnt
    method = stypes.strtocharpoint(method)
    target = stypes.strtocharpoint(target)
    et = ctypes.c_double(et)
    fixref = stypes.strtocharpoint(fixref)
    abcorr = stypes.strtocharpoint(abcorr)
    obsrvr = stypes.strtocharpoint(obsrvr)
    spoint = stypes.doubleVector(3)
    trgepc = ctypes.c_double(0)
    srfvec = stypes.doubleVector(3)
    libspice.subpnt_c(method, target, et, fixref, abcorr, obsrvr, spoint, ctypes.byref(trgepc), srfvec)
    return stypes.vectorToList(spoint), trgepc.value, stypes.vectorToList(srfvec)


def subpt(method, target, et, abcorr, obsrvr):
    #Todo: test subpt
    method = stypes.strtocharpoint(method)
    target = stypes.strtocharpoint(target)
    et = ctypes.c_double(et)
    abcorr = stypes.strtocharpoint(abcorr)
    obsrvr = stypes.strtocharpoint(obsrvr)
    spoint = stypes.doubleVector(3)
    alt = ctypes.c_double()
    libspice.subpt_c(method, target, et, abcorr, obsrvr, spoint, ctypes.byref(alt))
    return stypes.vectorToList(spoint), alt.value


def subslr(method, target, et, fixref, abcorr, obsrvr):
    #Todo: test subslr
    method = stypes.strtocharpoint(method)
    target = stypes.strtocharpoint(target)
    et = ctypes.c_double(et)
    fixref = stypes.strtocharpoint(fixref)
    abcorr = stypes.strtocharpoint(abcorr)
    obsrvr = stypes.strtocharpoint(obsrvr)
    spoint = stypes.doubleVector(3)
    trgepc = ctypes.c_double(0)
    srfvec = stypes.doubleVector(3)
    libspice.subslr_c(method, target, et, fixref, abcorr, obsrvr, spoint, ctypes.byref(trgepc), srfvec)
    return stypes.vectorToList(spoint), trgepc.value, stypes.vectorToList(srfvec)


def subsol(method, target, et, abcorr, obsrvr):
    #Todo: test subsol
    method = stypes.strtocharpoint(method)
    target = stypes.strtocharpoint(target)
    et = ctypes.c_double(et)
    abcorr = stypes.strtocharpoint(abcorr)
    obsrvr = stypes.strtocharpoint(obsrvr)
    spoint = stypes.doubleVector(3)
    libspice.subsol_c(method, target, et, abcorr, obsrvr, spoint)
    return stypes.vectorToList(spoint)


def sumad(array, n):
    array = stypes.toDoubleVector(array)
    n = ctypes.c_int(n)
    return libspice.sumad_c(array, n)


def sumai(array, n):
    array = stypes.toIntVector(array)
    n = ctypes.c_int(n)
    return libspice.sumai_c(array, n)


def surfnm(a, b, c, point):
    #Todo: test surfnm
    a = ctypes.c_double(a)
    b = ctypes.c_double(b)
    c = ctypes.c_double(c)
    point = stypes.toDoubleVector(point)
    normal = stypes.doubleVector(3)
    libspice.surfnm_c(a, b, c, point, normal)
    return stypes.vectorToList(normal)


def surfpt(positn, u, a, b, c):
    #Todo: test surfpt
    a = ctypes.c_double(a)
    b = ctypes.c_double(b)
    c = ctypes.c_double(c)
    positn = stypes.toDoubleVector(positn)
    u = stypes.toDoubleVector(u)
    point = stypes.doubleVector(3)
    found = ctypes.c_bool()
    libspice.surfpt_c(positn, u, a, b, c, point, ctypes.byref(found))
    return stypes.vectorToList(point), found.value


def surfpv(stvrtx, stdir, a, b, c):
    #Todo: test surfpv
    a = ctypes.c_double(a)
    b = ctypes.c_double(b)
    c = ctypes.c_double(c)
    stvrtx = stypes.toDoubleVector(stvrtx)
    stdir = stypes.toDoubleVector(stdir)
    stx = stypes.doubleVector(6)
    found = ctypes.c_bool()
    libspice.surfpv_c(stvrtx, stdir, a, b, c, stx, ctypes.byref(found))
    return stypes.vectorToList(stx), found.value


def swpool(agent, nnames, lenvals, names):
    #Todo: test swpool
    agent = stypes.strtocharpoint(agent)
    nnames = ctypes.c_int(nnames)
    lenvals = ctypes.c_int(lenvals)
    names = stypes.listtocharvector(names)
    libspice.swpool_c(agent, nnames, lenvals, names)
    pass


def sxfrom(instring, tostring, et):
    #Todo: test sxform
    instring = stypes.strtocharpoint(instring)
    tostring = stypes.strtocharpoint(tostring)
    et = ctypes.c_double(et)
    xform = stypes.doubleMatrix(x=6, y=6)
    libspice.sxform_c(instring, tostring, et, xform)
    return stypes.matrixToList(xform)


def szpool(name):
    name = stypes.strtocharpoint(name)
    n = ctypes.c_int()
    found = ctypes.c_bool(0)
    libspice.szpool_c(name, ctypes.byref(n), ctypes.byref(found))
    return n, found.value


########################################################################################################################
# T


def timdef(action, item, lenout, value=None):
    #todo: test
    action = stypes.strtocharpoint(action)
    item = stypes.strtocharpoint(item)
    lenout = ctypes.c_int(lenout)
    if value is None:
        value = stypes.strtocharpoint(" "*lenout.value)
    else:
        value = stypes.strtocharpoint(value)
    libspice.timdef_c(action, item, lenout, value)
    return value


def timout(et, pictur, lenout):
    #todo: test
    pictur = stypes.strtocharpoint(pictur)
    output = stypes.strtocharpoint(" " * lenout)
    et = ctypes.c_double(et)
    lenout = ctypes.c_int(lenout)
    libspice.timout_c(et, pictur, lenout, output)
    return output


def tipbod(ref, body, et):
    #Todo: test
    ref = stypes.strtocharpoint(ref)
    body = ctypes.c_int(body)
    et = ctypes.c_int(et)
    retmatrix = stypes.doubleMatrix()
    libspice.tipbod_c(ref, body, et, retmatrix)
    return stypes.matrixToList(retmatrix)


def tisbod(ref, body, et):
    #Todo: test tisbod
    ref = stypes.strtocharpoint(ref)
    body = ctypes.c_int(body)
    et = ctypes.c_int(et)
    retmatrix = stypes.doubleMatrix(x=6, y=6)
    libspice.tisbod_c(ref, body, et, retmatrix)
    return stypes.matrixToList(retmatrix)


def tkvrsn(item):
    item = stypes.strtocharpoint(item)
    return libspice.tkvrsn_c(item)


def tparse(instring, lenout):
    #Todo: test tparse
    errmsg = stypes.strtocharpoint(lenout)
    lenout = ctypes.c_int(lenout)
    instring = stypes.strtocharpoint(instring)
    sp2000 = ctypes.c_double()
    libspice.tparse_c(instring, lenout, ctypes.POINTER(sp2000), errmsg)
    return sp2000.value, errmsg


def tpictr(sample, lenout, lenerr):
    #Todo: test tpictr
    sample = stypes.strtocharpoint(sample)
    pictur = stypes.strtocharpoint(lenout)
    errmsg = stypes.strtocharpoint(lenerr)
    lenout = ctypes.c_int(lenout)
    lenerr = ctypes.c_int(lenerr)
    ok = ctypes.c_bool()
    libspice.tpictr_c(sample, lenout, lenerr, pictur, ctypes.byref(ok), errmsg)
    return pictur.value, ok.value, errmsg.value


def trace(matrix):
    #Todo: test trace
    matrix = stypes.listtodoublematrix(matrix)
    return libspice.trace_c(matrix)


def trcoff():
    #Todo: test trcoff
    libspice.trcoff_c()
    pass


def tsetyr(year):
    #Todo: test tsetyr
    year = ctypes.c_int(year)
    libspice.tsetyr_c(year)
    pass


def twopi():
    return libspice.twopi_c()


def twovec(axdef, indexa, plndef, indexp):
    #Todo: Test twovec
    axdef = stypes.toDoubleVector(axdef)
    indexa = ctypes.c_int(indexa)
    plndef = stypes.toDoubleVector(plndef)
    indexp = ctypes.c_int(indexp)
    mout = stypes.doubleMatrix()
    libspice.twovec_c(axdef, indexa, plndef, indexp, mout)
    return stypes.matrixToList(mout)


def tyear():
    #Todo: Test tyear
    return libspice.tyear_c()


########################################################################################################################
# U

def ucase(inchar, lenout):
    inchar = stypes.strtocharpoint(inchar)
    outchar = stypes.strtocharpoint(lenout)
    lenout = ctypes.c_int(lenout)
    libspice.ucase_c(inchar, lenout, outchar)
    return outchar.value


def ucrss(v1, v2):
    #Todo: test ucrss
    v1 = stypes.toDoubleVector(v1)
    v2 = stypes.toDoubleVector(v2)
    vout = stypes.doubleVector(3)
    libspice.ucrss_c(v1, v2, vout)
    return stypes.vectorToList(vout)


#UDDC # callback?


#UDDF # callback?


def union(a, b):
    #Todo: test union
    assert isinstance(a, stypes.SpiceCell)
    assert isinstance(b, stypes.SpiceCell)
    assert a.dtype == b.dtype
    assert a.dtype == 0 or a.dtype == 1 or a.dtype == 2
    if a.dtype is 0:
        c = stypes.SPICECHAR_CELL(a.size+b.size, a.length+b.length)
    if a.dtype is 1:
        c = stypes.SPICEDOUBLE_CELL(a.size+b.size)
    elif a.dtype is 2:
        c = stypes.SPICEINT_CELL(a.size+b.size)
    else:
        raise NotImplementedError
    libspice.union_c(ctypes.byref(a), ctypes.byref(b), ctypes.byref(c))
    return c


def unitim(epoch, insys, outsys):
    #Todo: test unitim
    epoch = ctypes.c_double(epoch)
    insys = stypes.strtocharpoint(insys)
    outsys = stypes.strtocharpoint(outsys)
    return libspice.unitim_c(epoch, insys, outsys)


def unload(filename):
    filename = stypes.strtocharpoint(filename)
    libspice.unload_c(filename)
    pass


def unorm(v1):
    v1 = stypes.toDoubleVector(v1)
    vout = stypes.doubleVector(3)
    vmag = ctypes.c_double()
    libspice.unorm_c(v1, vout, ctypes.byref(vmag))
    return stypes.vectorToList(vout), vmag.value


def unormg(v1, ndim):
    v1 = stypes.toDoubleVector(v1)
    vout = stypes.doubleVector(ndim)
    vmag = ctypes.c_double()
    ndim = ctypes.c_int(ndim)
    libspice.unormg_c(v1, ndim, vout, ctypes.byref(vmag))
    return stypes.vectorToList(vout), vmag.value


def utc2et(utcstr):
    #Todo: test utc2et
    utcstr = stypes.strtocharpoint(utcstr)
    et = ctypes.c_double()
    libspice.utc2et_c(utcstr, ctypes.byref(et))
    return et.value
########################################################################################################################
# V


def vadd(v1, v2):
    v1 = stypes.toDoubleVector(v1)
    v2 = stypes.toDoubleVector(v2)
    vout = stypes.doubleVector(3)
    libspice.vadd_c(v1, v2, vout)
    return stypes.vectorToList(vout)


def vaddg(v1, v2, ndim):
    v1 = stypes.toDoubleVector(v1)
    v2 = stypes.toDoubleVector(v2)
    vout = stypes.doubleVector(ndim)
    ndim = ctypes.c_int(ndim)
    libspice.vaddg_c(v1, v2, ndim, vout)
    return stypes.vectorToList(vout)


def valid(insize, n, inset):
    #Todo: test valid
    assert isinstance(inset, stypes.SpiceCell)
    insize = ctypes.c_int(insize)
    n = ctypes.c_int(n)
    libspice.valid_c(insize, n, ctypes.byref(inset))
    return inset


def vcrss(v1, v2):
    v1 = stypes.toDoubleVector(v1)
    v2 = stypes.toDoubleVector(v2)
    vout = stypes.doubleVector(3)
    libspice.vcrss_c(v1, v2, vout)
    return stypes.vectorToList(vout)


def vdist(v1, v2):
    v1 = stypes.toDoubleVector(v1)
    v2 = stypes.toDoubleVector(v2)
    return libspice.vdist_c(v1, v2)


def vdistg(v1, v2, ndim):
    #Todo: test vdistg
    v1 = stypes.toDoubleVector(v1)
    v2 = stypes.toDoubleVector(v2)
    ndim = ctypes.c_int(ndim)
    return libspice.vdistg_c(v1, v2, ndim)


def vdot(v1, v2):
    #Works but not verified, this would take all of 2 seconds to do however
    v1 = stypes.toDoubleVector(v1)
    v2 = stypes.toDoubleVector(v2)
    return libspice.vdot_c(v1, v2)


def vdotg(v1, v2, ndim):
    #Works but not verified, this would take all of 2 seconds to do however
    v1 = stypes.toDoubleVector(v1)
    v2 = stypes.toDoubleVector(v2)
    ndim = ctypes.c_int(ndim)
    return libspice.vdotg_c(v1, v2, ndim)


def vequ(v1):
    v1 = stypes.toDoubleVector(v1)
    vout = stypes.doubleVector(3)
    libspice.vequ_c(v1, vout)
    return stypes.vectorToList(vout)


def vequg(v1, ndim):
    v1 = stypes.toDoubleVector(v1)
    vout = stypes.doubleVector(ndim)
    ndim = ctypes.c_int(ndim)
    libspice.vequg_c(v1, ndim, vout)
    return stypes.vectorToList(vout)


def vhat(v1):
    v1 = stypes.toDoubleVector(v1)
    vout = stypes.doubleVector(3)
    libspice.vhat_c(v1, vout)
    return stypes.vectorToList(vout)


def vhatg(v1, ndim):
    v1 = stypes.toDoubleVector(v1)
    vout = stypes.doubleVector(ndim)
    ndim = ctypes.c_int(ndim)
    libspice.vhatg_c(v1, ndim, vout)
    return stypes.vectorToList(vout)


def vlcom(a, v1, b, v2):
    #Todo: test
    v1 = stypes.toDoubleVector(v1)
    v2 = stypes.toDoubleVector(v2)
    sumv = stypes.doubleVector(3)
    a = ctypes.c_double(a)
    b = ctypes.c_double(b)
    libspice.vlcom_c(a, v1, b, v2, sumv)
    return stypes.vectorToList(sumv)


def vlcom3(a, v1, b, v2, c, v3):
    #Todo: test
    v1 = stypes.toDoubleVector(v1)
    v2 = stypes.toDoubleVector(v2)
    v3 = stypes.toDoubleVector(v3)
    sumv = stypes.doubleVector(3)
    a = ctypes.c_double(a)
    b = ctypes.c_double(b)
    c = ctypes.c_double(c)
    libspice.vlcom3_c(a, v1, b, v2, c, v3, sumv)
    return stypes.vectorToList(sumv)


def vlcomg(n, a, v1, b, v2):
    #Todo: test
    v1 = stypes.toDoubleVector(v1)
    v2 = stypes.toDoubleVector(v2)
    sumv = stypes.doubleVector(n)
    a = ctypes.c_double(a)
    b = ctypes.c_double(b)
    n = ctypes.c_int(n)
    libspice.vlcomg_c(n, a, v1, b, v2, sumv)
    return stypes.vectorToList(sumv)


def vminug(vin, ndim):
    #todo: test
    vin = stypes.toDoubleVector(vin)
    vout = stypes.doubleVector(ndim)
    ndim = ctypes.c_int(ndim)
    libspice.vminug_c(vin, ndim, vout)
    return stypes.vectorToList(vout)


def vminus(vin):
    #todo: test
    vin = stypes.toDoubleVector(vin)
    vout = stypes.doubleVector(3)
    libspice.vminus_c(vin, vout)
    return stypes.vectorToList(vout)


def vnorm(v):
    v = stypes.toDoubleVector(v)
    return libspice.vnorm_c(v)


def vnormg(v, ndim):
    #todo: test
    v = stypes.toDoubleVector(v)
    ndim = ctypes.c_int(ndim)
    return libspice.vnormg_c(v, ndim)


def vpack(x, y, z):
    x = ctypes.c_double(x)
    y = ctypes.c_double(y)
    z = ctypes.c_double(z)
    vout = stypes.doubleVector(3)
    libspice.vpack_c(x, y, z, vout)
    return stypes.vectorToList(vout)


def vperp(a, b):
    a = stypes.toDoubleVector(a)
    b = stypes.toDoubleVector(b)
    vout = stypes.doubleVector(3)
    libspice.vperp_c(a, b, vout)
    return stypes.vectorToList(vout)


def vprjp(vin, plane):
    vin = stypes.toDoubleVector(vin)
    vout = stypes.doubleVector(3)
    libspice.vprjp_c(vin, ctypes.byref(plane), vout)
    return stypes.vectorToList(vout)


def vprjpi(vin, projpl, invpl):
    vin = stypes.toDoubleVector(vin)
    vout = stypes.doubleVector(3)
    found = ctypes.c_bool()
    libspice.vprjpi_c(vin, ctypes.byref(projpl), ctypes.byref(invpl), vout, ctypes.byref(found))
    return stypes.vectorToList(vout), found.value


def vproj(a, b):
    a = stypes.toDoubleVector(a)
    b = stypes.toDoubleVector(b)
    vout = stypes.doubleVector(3)
    libspice.vproj_c(a, b, vout)
    return stypes.vectorToList(vout)


def vrel(v1, v2):
    v1 = stypes.toDoubleVector(v1)
    v2 = stypes.toDoubleVector(v2)
    return libspice.vrel_c(v1, v2)


def vrelg(v1, v2, ndim):
    #Todo: test
    v1 = stypes.toDoubleVector(v1)
    v2 = stypes.toDoubleVector(v2)
    ndim = ctypes.c_int(ndim)
    return libspice.vrelg_c(v1, v2, ndim)


def vrotv(v, axis, theta):
    #Tested, but clarly some rounding issues exist (0 as 6.123*10^-17, etc)
    # halfpi is not exactly reprentable in IEEE 754 notation,
    v = stypes.toDoubleVector(v)
    axis = stypes.toDoubleVector(axis)
    theta = ctypes.c_double(theta)
    r = stypes.doubleVector(3)
    libspice.vrotv_c(v, axis, theta, r)
    return stypes.vectorToList(r)


def vscl(s, v1):
    #Todo: test
    s = ctypes.c_double(s)
    v1 = stypes.toDoubleVector(v1)
    vout = stypes.doubleVector(3)
    libspice.vscl_c(s, v1, vout)
    return stypes.vectorToList(vout)


def vsclg(s, v1, ndim):
    #Todo: test
    s = ctypes.c_double(s)
    v1 = stypes.toDoubleVector(v1)
    vout = stypes.doubleVector(ndim)
    ndim = ctypes.c_int(ndim)
    libspice.vsclg_c(s, v1, ndim, vout)
    return stypes.vectorToList(vout)


def vsep(v1, v2):
    #Todo: test
    v1 = stypes.toDoubleVector(v1)
    v2 = stypes.toDoubleVector(v2)
    return libspice.vsep_c(v1, v2)


def vsepg(v1, v2, ndim):
    #Todo: test
    v1 = stypes.toDoubleVector(v1)
    v2 = stypes.toDoubleVector(v2)
    ndim = ctypes.c_int(ndim)
    return libspice.vsepg_c(v1, v2, ndim)


def vsub(v1, v2):
    #Todo: test
    v1 = stypes.toDoubleVector(v1)
    v2 = stypes.toDoubleVector(v2)
    vout = stypes.doubleVector(3)
    libspice.vsub_c(v1, v2, vout)
    return stypes.vectorToList(vout)


def vsubg(v1, v2, ndim):
    #Todo: test
    v1 = stypes.toDoubleVector(v1)
    v2 = stypes.toDoubleVector(v2)
    vout = stypes.doubleVector(ndim)
    ndim = stypes.ctypes.c_int(ndim)
    libspice.vsubg_c(v1, v2, ndim, vout)
    return stypes.vectorToList(vout)


def vtmv(v1, matrix, v2):
    v1 = stypes.toDoubleVector(v1)
    matrix = stypes.listtodoublematrix(matrix)
    v2 = stypes.toDoubleVector(v2)
    return libspice.vtmv_c(v1, matrix, v2)


def vtmvg(v1, matrix, v2, nrow, ncol):
    v1 = stypes.toDoubleVector(v1)
    matrix = stypes.listtodoublematrix(matrix, x=ncol, y=nrow)
    v2 = stypes.toDoubleVector(v2)
    nrow = ctypes.c_int(nrow)
    ncol = ctypes.c_int(ncol)
    return libspice.vtmvg_c(v1, matrix, v2, nrow, ncol)


def vupack(v):
    v1 = stypes.toDoubleVector(v)
    x = ctypes.c_double()
    y = ctypes.c_double()
    z = ctypes.c_double()
    libspice.vupack_c(v1, ctypes.byref(x), ctypes.byref(y), ctypes.byref(z))
    return x.value, y.value, z.value


def vzero(v):
    """

    :rtype : bool
    :param v: Double Vector of length 3
    :return: True if all values equal zero, false else.

    #test
    >>> vzero([0.0,0.0,1.0])
    False
    >>> vzero([0.0,0.0,0.0])
    True
    >>> vzero(numpy.array([0.0,0.0,1.0]))
    False
    >>> vzero(numpy.array([0.0,0.0,0.0]))
    True

    """
    v = stypes.toDoubleVector(v)
    return libspice.vzero_c(v)


def vzerog(v, ndim):
    """

    :rtype : bool
    :param v: Double Vector of length ndim
    :param ndim: length of v
    :return: True if all values equal zero, false else.

    #test
    >>> vzerog([0.0,1.0], 2)
    False
    >>> vzerog([0.0,0.0], 2)
    True
    >>> vzerog(numpy.array([0.0,0.0,1.0,0.0]), 4)
    False
    >>> vzerog(numpy.array([0.0,0.0,0.0,0.0]), 4)
    True

    """
    v = stypes.toDoubleVector(v)
    ndim = stypes.ctypes.c_int(ndim)
    return libspice.vzerog_c(v, ndim)

########################################################################################################################
# W


def wncard(window):
    assert isinstance(window, stypes.SpiceCell)
    return libspice.wncard_c(window)


def wncomd(left, right, window):
    #Todo: test wncomd
    assert isinstance(window, stypes.SpiceCell)
    assert window.dtype == 1
    left = ctypes.c_double(left)
    right = ctypes.c_double(right)
    result = stypes.SpiceCell.double(window.size)
    libspice.wncomd_c(left, right, ctypes.byref(window), result)
    return result


def wncond(left, right, window):
    #Todo: test wncond
    assert isinstance(window, stypes.SpiceCell)
    assert window.dtype == 1
    left = ctypes.c_double(left)
    right = ctypes.c_double(right)
    libspice.wncond_c(left, right, ctypes.byref(window))
    return window


def wndifd(a, b):
    #Todo: test wndifd
    assert isinstance(a, stypes.SpiceCell)
    assert isinstance(b, stypes.SpiceCell)
    assert a.dtype == 1
    assert b.dtype == 1
    c = stypes.SpiceCell.double(a.size+b.size)
    libspice.wndifd_c(ctypes.byref(a), ctypes.byref(b), ctypes.byref(c))
    return c


def wnelmd(point, window):
    #Todo: test wnelmd
    assert isinstance(window, stypes.SpiceCell)
    assert window.dtype == 1
    point = ctypes.c_double(point)
    return libspice.wnelmd_c(point, ctypes.byref(window))


def wnexpd(left, right, window):
    #Todo: test wnexpd
    assert isinstance(window, stypes.SpiceCell)
    assert window.dtype == 1
    left = ctypes.c_double(left)
    right = ctypes.c_double(right)
    libspice.wnexpd_c(left, right, ctypes.byref(window))
    return window


def wnextd(side, window):
    #Todo: test wnextd
    assert isinstance(window, stypes.SpiceCell)
    assert window.dtype == 1
    assert side == 'L' or side == 'R'
    side = ctypes.c_char(side)
    libspice.wnextd_c(side, ctypes.byref(window))
    return window


def wnfetd(window, n):
    #Todo: test wnfetd
    assert isinstance(window, stypes.SpiceCell)
    assert window.dtype == 1
    n = ctypes.c_int(n)
    left = ctypes.c_double()
    right = ctypes.c_double()
    libspice.wnfetd_c(ctypes.byref(window), n, ctypes.byref(left), ctypes.byref(right))
    return left.value, right.value


def wnfild(small, window):
    #Todo: test wnfild
    assert isinstance(window, stypes.SpiceCell)
    assert window.dtype == 1
    small = ctypes.c_double(small)
    libspice.wnfild_c(small, ctypes.byref(window))
    return window


def wnfltd(small, window):
    #Todo: test wnfltd
    assert isinstance(window, stypes.SpiceCell)
    assert window.dtype == 1
    small = ctypes.c_double(small)
    libspice.wnfltd_c(small, ctypes.byref(window))
    return window


def wnincd(left, right, window):
    #Todo: test wnincd
    assert isinstance(window, stypes.SpiceCell)
    assert window.dtype == 1
    left = ctypes.c_double(left)
    right = ctypes.c_double(right)
    return libspice.wnincd_c(left, right, ctypes.byref(window))


def wninsd(left, right, window):
    #Todo: test wninsd
    assert isinstance(window, stypes.SpiceCell)
    assert window.dtype == 1
    left = ctypes.c_double(left)
    right = ctypes.c_double(right)
    libspice.wninsd_c(left, right, ctypes.byref(window))
    return window


def wnintd(a, b):
    #Todo: test wnintd
    assert isinstance(a, stypes.SpiceCell)
    assert b.dtype == 1
    assert isinstance(b, stypes.SpiceCell)
    assert a.dtype == 1
    c = stypes.SpiceCell.double(b.size+a.size)
    libspice.wnintd_c(ctypes.byref(a), ctypes.byref(b), ctypes.byref(c))
    return c


def wnreld(a, op, b):
    #Todo: test wnreld
    assert isinstance(a, stypes.SpiceCell)
    assert b.dtype == 1
    assert isinstance(b, stypes.SpiceCell)
    assert a.dtype == 1
    assert isinstance(op, str)
    op = stypes.strtocharpoint(op)
    return libspice.wnreld_c(ctypes.byref(a), op, ctypes.byref(b))


def wnsumd(window):
    #Todo: test wnsumd
    assert isinstance(window, stypes.SpiceCell)
    assert window.dtype == 1
    meas = ctypes.c_double()
    avg = ctypes.c_double()
    stddev = ctypes.c_double()
    shortest = ctypes.c_int()
    longest = ctypes.c_int()
    libspice.wnsumd_c(ctypes.byref(window), ctypes.byref(meas), ctypes.byref(avg), ctypes.byref(stddev), ctypes.byref(shortest), ctypes.byref(longest))
    return meas.value, avg.value, stddev.value, shortest.value, longest.value


def wnunid(a, b):
    #Todo: test wnunid
    assert isinstance(a, stypes.SpiceCell)
    assert b.dtype == 1
    assert isinstance(b, stypes.SpiceCell)
    assert a.dtype == 1
    c = stypes.SpiceCell.double(b.size+a.size)
    libspice.wnunid_c(ctypes.byref(a), ctypes.byref(b), ctypes.byref(c))
    return c


def wnvald(insize, n, window):
    #Todo: test wnvalid
    assert isinstance(window, stypes.SpiceCell)
    assert window.dtype == 1
    insize = ctypes.c_int(insize)
    n = ctypes.c_int(n)
    libspice.wnvald_c(insize, n, ctypes.byref(window))
    return window


########################################################################################################################
# X

def xf2eul(xform, axisa, axisb, axisc):
    #Todo: test xf2eul
    xform = stypes.listtodoublematrix(xform, x=6, y=6)
    axisa = ctypes.c_int(axisa)
    axisb = ctypes.c_int(axisb)
    axisc = ctypes.c_int(axisc)
    eulang = stypes.doubleVector(6)
    unique = ctypes.c_bool()
    libspice.xf2eul_c(xform, axisa, axisb, axisc, eulang, unique)
    return stypes.vectorToList(eulang), unique.value


def xf2rav(xform):
    xform = stypes.listtodoublematrix(xform, x=6, y=6)
    rot = stypes.doubleMatrix()
    av = stypes.doubleVector(3)
    libspice.xf2rav_c(xform, rot, av)
    return stypes.matrixToList(rot), stypes.vectorToList(av)


def xpose(m):
    m = stypes.toDoubleMatrix(m)
    mout = stypes.doubleMatrix(x=3, y=3)
    libspice.xpose_c(m, mout)
    return stypes.matrixToList(mout)


def xpose6(m):
    m = stypes.toDoubleMatrix(m)
    mout = stypes.doubleMatrix(x=6, y=6)
    libspice.xpose6_c(m, mout)
    return stypes.matrixToList(mout)


def xposeg(matrix, nrow, ncol):
    matrix = stypes.listtodoublematrix(matrix, x=ncol, y=nrow)
    mout = stypes.doubleMatrix(x=ncol, y=nrow)
    ncol = ctypes.c_int(ncol)
    nrow = ctypes.c_int(nrow)
    libspice.xposeg_c(matrix, nrow, ncol, mout)
    return stypes.matrixToList(mout)