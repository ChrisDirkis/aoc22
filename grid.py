from itertools import permutations, chain, product
from collections import namedtuple
from math import sqrt, prod

vec2 = namedtuple('vec2', ['x', 'y'])
vec3 = namedtuple('vec3', ['x', 'y', 'z'])
vec4 = namedtuple('vec4', ['x', 'y', 'z', 'w'])

def to_vec(t):
    if len(t) == 2:
        return vec2(*t)
    elif len(t) == 3:
        return vec3(*t)
    elif len(t) == 4:
        return vec4(*t)
    return t

def add_t(a, b):
    return to_vec(tuple(sum(v) for v in zip(a, b)))

def sub_t(a, b):
    return to_vec(tuple(v1 - v2 for v1, v2 in zip(a, b)))

def dot_t(a, b):
    return to_vec(tuple(prod(v) for v in zip(a, b)))

def in_grid(addr, dims):
    return all(v >= 0 and v < dims[i] for i, v in enumerate(addr))

def all_addrs(dims):
    return (to_vec(v) for v in product(*(list(range(v) for v in dims))))

def index_into(grid, addr):
    arr = grid
    for v in reversed(addr):
        arr = arr[v]
    return arr

def find_addrs_v(grid, dims, value):
    return (addr for addr in all_addrs(dims) if index_into(grid, addr) == value)

def find_addrs_l(grid, dims, func):
    return (addr for addr in all_addrs(dims) if func(index_into(grid, addr)))

def gen_grid(dims):
    if len(dims) == 1:
        return [0] * dims[0]
    super_dims = tuple(dims[1:])
    return [gen_grid(super_dims) for _ in range(dims[0])]

def iter_grid(grid):
    if not isinstance(grid, list):
        return [grid]
    if not isinstance(grid[0], list):
        return grid
    return chain(*(iter_grid(subgrid) for subgrid in grid))

def adj(addr, dims):
    n = len(addr)
    offsets = chain(permutations([1] + [0] * (n - 1)), permutations([-1] + [0] * (n - 1)))
    adjs = (add_t(addr, offset) for offset in offsets)
    return (adj for adj in adjs if in_grid(addr, dims))

def adj_diag(addr, dims):
    offsets = (v for v in product([-1, 0, 1], repeat=len(dims)) if any(v))
    adjs = (add_t(addr, offset) for offset in offsets)
    return (adj for adj in adjs if in_grid(addr, dims))

def len_euclid(addr):
    return sqrt(sum(v**2 for v in addr))

def len_taxi(addr):
    return sum(abs(v) for v in addr)