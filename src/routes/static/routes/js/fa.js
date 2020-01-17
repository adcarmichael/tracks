!function () {
    "use strict";
    var c = {}
        , l = {};
    try {
        "undefined" != typeof window && (c = window),
            "undefined" != typeof document && (l = document)
    } catch (c) { }
    var h = (c.navigator || {}).userAgent
        , z = void 0 === h ? "" : h
        , v = c
        , a = l
        , m = (v.document,
            !!a.documentElement && !!a.head && "function" == typeof a.addEventListener && a.createElement,
            ~z.indexOf("MSIE") || z.indexOf("Trident/"),
            "___FONT_AWESOME___")
        , s = function () {
            try {
                return !0
            } catch (c) {
                return !1
            }
        }();
    var e = v || {};
    e[m] || (e[m] = {}),
        e[m].styles || (e[m].styles = {}),
        e[m].hooks || (e[m].hooks = {}),
        e[m].shims || (e[m].shims = []);
    var t = e[m];
    function M(c, z) {
        var l = (2 < arguments.length && void 0 !== arguments[2] ? arguments[2] : {}).skipHooks
            , h = void 0 !== l && l
            , v = Object.keys(z).reduce(function (c, l) {
                var h = z[l];
                return !!h.icon ? c[h.iconName] = h.icon : c[l] = h,
                    c
            }, {});
        "function" != typeof t.hooks.addPack || h ? t.styles[c] = function (v) {
            for (var c = 1; c < arguments.length; c++) {
                var a = null != arguments[c] ? arguments[c] : {}
                    , l = Object.keys(a);
                "function" == typeof Object.getOwnPropertySymbols && (l = l.concat(Object.getOwnPropertySymbols(a).filter(function (c) {
                    return Object.getOwnPropertyDescriptor(a, c).enumerable
                }))),
                    l.forEach(function (c) {
                        var l, h, z;
                        l = v,
                            z = a[h = c],
                            h in l ? Object.defineProperty(l, h, {
                                value: z,
                                enumerable: !0,
                                configurable: !0,
                                writable: !0
                            }) : l[h] = z
                    })
            }
            return v
        }({}, t.styles[c] || {}, v) : t.hooks.addPack(c, v),
            "fas" === c && M("fa", z)
    }
    var f = {
        zhihu: [640, 512, [], "f63f", "M170.54 148.13v217.54l23.43.01 7.71 26.37 42.01-26.37h49.53V148.13H170.54zm97.75 193.93h-27.94l-27.9 17.51-5.08-17.47-11.9-.04V171.75h72.82v170.31zm-118.46-94.39H97.5c1.74-27.1 2.2-51.59 2.2-73.46h51.16s1.97-22.56-8.58-22.31h-88.5c3.49-13.12 7.87-26.66 13.12-40.67 0 0-24.07 0-32.27 21.57-3.39 8.9-13.21 43.14-30.7 78.12 5.89-.64 25.37-1.18 36.84-22.21 2.11-5.89 2.51-6.66 5.14-14.53h28.87c0 10.5-1.2 66.88-1.68 73.44H20.83c-11.74 0-15.56 23.62-15.56 23.62h65.58C66.45 321.1 42.83 363.12 0 396.34c20.49 5.85 40.91-.93 51-9.9 0 0 22.98-20.9 35.59-69.25l53.96 64.94s7.91-26.89-1.24-39.99c-7.58-8.92-28.06-33.06-36.79-41.81L87.9 311.95c4.36-13.98 6.99-27.55 7.87-40.67h61.65s-.09-23.62-7.59-23.62v.01zm412.02-1.6c20.83-25.64 44.98-58.57 44.98-58.57s-18.65-14.8-27.38-4.06c-6 8.15-36.83 48.2-36.83 48.2l19.23 14.43zm-150.09-59.09c-9.01-8.25-25.91 2.13-25.91 2.13s39.52 55.04 41.12 57.45l19.46-13.73s-25.67-37.61-34.66-45.86h-.01zM640 258.35c-19.78 0-130.91.93-131.06.93v-101c4.81 0 12.42-.4 22.85-1.2 40.88-2.41 70.13-4 87.77-4.81 0 0 12.22-27.19-.59-33.44-3.07-1.18-23.17 4.58-23.17 4.58s-165.22 16.49-232.36 18.05c1.6 8.82 7.62 17.08 15.78 19.55 13.31 3.48 22.69 1.7 49.15.89 24.83-1.6 43.68-2.43 56.51-2.43v99.81H351.41s2.82 22.31 25.51 22.85h107.94v70.92c0 13.97-11.19 21.99-24.48 21.12-14.08.11-26.08-1.15-41.69-1.81 1.99 3.97 6.33 14.39 19.31 21.84 9.88 4.81 16.17 6.57 26.02 6.57 29.56 0 45.67-17.28 44.89-45.31v-73.32h122.36c9.68 0 8.7-23.78 8.7-23.78l.03-.01z"]
    };
    !function (c) {
        try {
            c()
        } catch (c) {
            if (!s)
                throw c
        }
    }(function () {
        M("fab", f)
    })
}(),
    function () {
        "use strict";
        var c = {}
            , l = {};
        try {
            "undefined" != typeof window && (c = window),
                "undefined" != typeof document && (l = document)
        } catch (c) { }
        var h = (c.navigator || {}).userAgent
            , z = void 0 === h ? "" : h
            , v = c
            , a = l
            , m = (v.document,
                !!a.documentElement && !!a.head && "function" == typeof a.addEventListener && a.createElement,
                ~z.indexOf("MSIE") || z.indexOf("Trident/"),
                "___FONT_AWESOME___")
            , s = function () {
                try {
                    return !0
                } catch (c) {
                    return !1
                }
            }();
        var e = v || {};
        e[m] || (e[m] = {}),
            e[m].styles || (e[m].styles = {}),
            e[m].hooks || (e[m].hooks = {}),
            e[m].shims || (e[m].shims = []);
        var t = e[m];
        function M(c, z) {
            var l = (2 < arguments.length && void 0 !== arguments[2] ? arguments[2] : {}).skipHooks
                , h = void 0 !== l && l
                , v = Object.keys(z).reduce(function (c, l) {
                    var h = z[l];
                    return !!h.icon ? c[h.iconName] = h.icon : c[l] = h,
                        c
                }, {});
            "function" != typeof t.hooks.addPack || h ? t.styles[c] = function (v) {
                for (var c = 1; c < arguments.length; c++) {
                    var a = null != arguments[c] ? arguments[c] : {}
                        , l = Object.keys(a);
                    "function" == typeof Object.getOwnPropertySymbols && (l = l.concat(Object.getOwnPropertySymbols(a).filter(function (c) {
                        return Object.getOwnPropertyDescriptor(a, c).enumerable
                    }))),
                        l.forEach(function (c) {
                            var l, h, z;
                            l = v,
                                z = a[h = c],
                                h in l ? Object.defineProperty(l, h, {
                                    value: z,
                                    enumerable: !0,
                                    configurable: !0,
                                    writable: !0
                                }) : l[h] = z
                        })
                }
                return v
            }({}, t.styles[c] || {}, v) : t.hooks.addPack(c, v),
                "fas" === c && M("fa", z)
        }
        var f = {
            "window-restore": [512, 512, [], "f2d2", "M464 0H144c-26.5 0-48 21.5-48 48v48H48c-26.5 0-48 21.5-48 48v320c0 26.5 21.5 48 48 48h320c26.5 0 48-21.5 48-48v-48h48c26.5 0 48-21.5 48-48V48c0-26.5-21.5-48-48-48zm-96 464H48V256h320v208zm96-96h-48V144c0-26.5-21.5-48-48-48H144V48h320v320z"]
        };
        !function (c) {
            try {
                c()
            } catch (c) {
                if (!s)
                    throw c
            }
        }(function () {
            M("far", f)
        })
    }(),
    function () {
        "use strict";
        var c = {}
            , l = {};
        try {
            "undefined" != typeof window && (c = window),
                "undefined" != typeof document && (l = document)
        } catch (c) { }
        var h = (c.navigator || {}).userAgent
            , z = void 0 === h ? "" : h
            , v = c
            , a = l
            , m = (v.document,
                !!a.documentElement && !!a.head && "function" == typeof a.addEventListener && a.createElement,
                ~z.indexOf("MSIE") || z.indexOf("Trident/"),
                "___FONT_AWESOME___")
            , s = function () {
                try {
                    return !0
                } catch (c) {
                    return !1
                }
            }();
        var e = v || {};
        e[m] || (e[m] = {}),
            e[m].styles || (e[m].styles = {}),
            e[m].hooks || (e[m].hooks = {}),
            e[m].shims || (e[m].shims = []);
        var t = e[m];
        function M(c, z) {
            var l = (2 < arguments.length && void 0 !== arguments[2] ? arguments[2] : {}).skipHooks
                , h = void 0 !== l && l
                , v = Object.keys(z).reduce(function (c, l) {
                    var h = z[l];
                    return !!h.icon ? c[h.iconName] = h.icon : c[l] = h,
                        c
                }, {});
            "function" != typeof t.hooks.addPack || h ? t.styles[c] = function (v) {
                for (var c = 1; c < arguments.length; c++) {
                    var a = null != arguments[c] ? arguments[c] : {}
                        , l = Object.keys(a);
                    "function" == typeof Object.getOwnPropertySymbols && (l = l.concat(Object.getOwnPropertySymbols(a).filter(function (c) {
                        return Object.getOwnPropertyDescriptor(a, c).enumerable
                    }))),
                        l.forEach(function (c) {
                            var l, h, z;
                            l = v,
                                z = a[h = c],
                                h in l ? Object.defineProperty(l, h, {
                                    value: z,
                                    enumerable: !0,
                                    configurable: !0,
                                    writable: !0
                                }) : l[h] = z
                        })
                }
                return v
            }({}, t.styles[c] || {}, v) : t.hooks.addPack(c, v),
                "fas" === c && M("fa", z)
        }
        var f = {




            "arrow-circle-down": [512, 512, [], "f0ab", "M504 256c0 137-111 248-248 248S8 393 8 256 119 8 256 8s248 111 248 248zm-143.6-28.9L288 302.6V120c0-13.3-10.7-24-24-24h-16c-13.3 0-24 10.7-24 24v182.6l-72.4-75.5c-9.3-9.7-24.8-9.9-34.3-.4l-10.9 11c-9.4 9.4-9.4 24.6 0 33.9L239 404.3c9.4 9.4 24.6 9.4 33.9 0l132.7-132.7c9.4-9.4 9.4-24.6 0-33.9l-10.9-11c-9.5-9.5-25-9.3-34.3.4z"],
            "arrow-circle-left": [512, 512, [], "f0a8", "M256 504C119 504 8 393 8 256S119 8 256 8s248 111 248 248-111 248-248 248zm28.9-143.6L209.4 288H392c13.3 0 24-10.7 24-24v-16c0-13.3-10.7-24-24-24H209.4l75.5-72.4c9.7-9.3 9.9-24.8.4-34.3l-11-10.9c-9.4-9.4-24.6-9.4-33.9 0L107.7 239c-9.4 9.4-9.4 24.6 0 33.9l132.7 132.7c9.4 9.4 24.6 9.4 33.9 0l11-10.9c9.5-9.5 9.3-25-.4-34.3z"],
            "arrow-circle-right": [512, 512, [], "f0a9", "M256 8c137 0 248 111 248 248S393 504 256 504 8 393 8 256 119 8 256 8zm-28.9 143.6l75.5 72.4H120c-13.3 0-24 10.7-24 24v16c0 13.3 10.7 24 24 24h182.6l-75.5 72.4c-9.7 9.3-9.9 24.8-.4 34.3l11 10.9c9.4 9.4 24.6 9.4 33.9 0L404.3 273c9.4-9.4 9.4-24.6 0-33.9L271.6 106.3c-9.4-9.4-24.6-9.4-33.9 0l-11 10.9c-9.5 9.6-9.3 25.1.4 34.4z"],
            "arrow-circle-up": [512, 512, [], "f0aa", "M8 256C8 119 119 8 256 8s248 111 248 248-111 248-248 248S8 393 8 256zm143.6 28.9l72.4-75.5V392c0 13.3 10.7 24 24 24h16c13.3 0 24-10.7 24-24V209.4l72.4 75.5c9.3 9.7 24.8 9.9 34.3.4l10.9-11c9.4-9.4 9.4-24.6 0-33.9L273 107.7c-9.4-9.4-24.6-9.4-33.9 0L106.3 240.4c-9.4 9.4-9.4 24.6 0 33.9l10.9 11c9.6 9.5 25.1 9.3 34.4-.4z"],


            bullseye: [496, 512, [], "f140", "M248 8C111.03 8 0 119.03 0 256s111.03 248 248 248 248-111.03 248-248S384.97 8 248 8zm0 432c-101.69 0-184-82.29-184-184 0-101.69 82.29-184 184-184 101.69 0 184 82.29 184 184 0 101.69-82.29 184-184 184zm0-312c-70.69 0-128 57.31-128 128s57.31 128 128 128 128-57.31 128-128-57.31-128-128-128zm0 192c-35.29 0-64-28.71-64-64s28.71-64 64-64 64 28.71 64 64-28.71 64-64 64z"],



            "chart-line": [512, 512, [], "f201", "M496 384H64V80c0-8.84-7.16-16-16-16H16C7.16 64 0 71.16 0 80v336c0 17.67 14.33 32 32 32h464c8.84 0 16-7.16 16-16v-32c0-8.84-7.16-16-16-16zM464 96H345.94c-21.38 0-32.09 25.85-16.97 40.97l32.4 32.4L288 242.75l-73.37-73.37c-12.5-12.5-32.76-12.5-45.25 0l-68.69 68.69c-6.25 6.25-6.25 16.38 0 22.63l22.62 22.62c6.25 6.25 16.38 6.25 22.63 0L192 237.25l73.37 73.37c12.5 12.5 32.76 12.5 45.25 0l96-96 32.4 32.4c15.12 15.12 40.97 4.41 40.97-16.97V112c.01-8.84-7.15-16-15.99-16z"],



            eye: [576, 512, [], "f06e", "M572.52 241.4C518.29 135.59 410.93 64 288 64S57.68 135.64 3.48 241.41a32.35 32.35 0 0 0 0 29.19C57.71 376.41 165.07 448 288 448s230.32-71.64 284.52-177.41a32.35 32.35 0 0 0 0-29.19zM288 400a144 144 0 1 1 144-144 143.93 143.93 0 0 1-144 144zm0-240a95.31 95.31 0 0 0-25.31 3.79 47.85 47.85 0 0 1-66.9 66.9A95.78 95.78 0 1 0 288 160z"],



            "hand-rock": [512, 512, [], "f255", "M464.8 80c-26.9-.4-48.8 21.2-48.8 48h-8V96.8c0-26.3-20.9-48.3-47.2-48.8-26.9-.4-48.8 21.2-48.8 48v32h-8V80.8c0-26.3-20.9-48.3-47.2-48.8-26.9-.4-48.8 21.2-48.8 48v48h-8V96.8c0-26.3-20.9-48.3-47.2-48.8-26.9-.4-48.8 21.2-48.8 48v136l-8-7.1v-48.1c0-26.3-20.9-48.3-47.2-48.8C21.9 127.6 0 149.2 0 176v66.4c0 27.4 11.7 53.5 32.2 71.8l111.7 99.3c10.2 9.1 16.1 22.2 16.1 35.9v6.7c0 13.3 10.7 24 24 24h240c13.3 0 24-10.7 24-24v-2.9c0-12.8 2.6-25.5 7.5-37.3l49-116.3c5-11.8 7.5-24.5 7.5-37.3V128.8c0-26.3-20.9-48.4-47.2-48.8z"],


        };
        !function (c) {
            try {
                c()
            } catch (c) {
                if (!s)
                    throw c
            }
        }(function () {
            M("fas", f)
        })
    }(),
    function () {
        "use strict";
        function a(c) {
            return (a = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (c) {
                return typeof c
            }
                : function (c) {
                    return c && "function" == typeof Symbol && c.constructor === Symbol && c !== Symbol.prototype ? "symbol" : typeof c
                }
            )(c)
        }
        function v(c, l) {
            for (var h = 0; h < l.length; h++) {
                var z = l[h];
                z.enumerable = z.enumerable || !1,
                    z.configurable = !0,
                    "value" in z && (z.writable = !0),
                    Object.defineProperty(c, z.key, z)
            }
        }
        function X(v) {
            for (var c = 1; c < arguments.length; c++) {
                var a = null != arguments[c] ? arguments[c] : {}
                    , l = Object.keys(a);
                "function" == typeof Object.getOwnPropertySymbols && (l = l.concat(Object.getOwnPropertySymbols(a).filter(function (c) {
                    return Object.getOwnPropertyDescriptor(a, c).enumerable
                }))),
                    l.forEach(function (c) {
                        var l, h, z;
                        l = v,
                            z = a[h = c],
                            h in l ? Object.defineProperty(l, h, {
                                value: z,
                                enumerable: !0,
                                configurable: !0,
                                writable: !0
                            }) : l[h] = z
                    })
            }
            return v
        }
        function r(c, l) {
            return function (c) {
                if (Array.isArray(c))
                    return c
            }(c) || function (c, l) {
                var h = []
                    , z = !0
                    , v = !1
                    , a = void 0;
                try {
                    for (var m, s = c[Symbol.iterator](); !(z = (m = s.next()).done) && (h.push(m.value),
                        !l || h.length !== l); z = !0)
                        ;
                } catch (c) {
                    v = !0,
                        a = c
                } finally {
                    try {
                        z || null == s.return || s.return()
                    } finally {
                        if (v)
                            throw a
                    }
                }
                return h
            }(c, l) || function () {
                throw new TypeError("Invalid attempt to destructure non-iterable instance")
            }()
        }
        function n(c) {
            return function (c) {
                if (Array.isArray(c)) {
                    for (var l = 0, h = new Array(c.length); l < c.length; l++)
                        h[l] = c[l];
                    return h
                }
            }(c) || function (c) {
                if (Symbol.iterator in Object(c) || "[object Arguments]" === Object.prototype.toString.call(c))
                    return Array.from(c)
            }(c) || function () {
                throw new TypeError("Invalid attempt to spread non-iterable instance")
            }()
        }
        var c = function () { }
            , l = {}
            , h = {}
            , z = null
            , m = {
                mark: c,
                measure: c
            };
        try {
            "undefined" != typeof window && (l = window),
                "undefined" != typeof document && (h = document),
                "undefined" != typeof MutationObserver && (z = MutationObserver),
                "undefined" != typeof performance && (m = performance)
        } catch (c) { }
        var s = (l.navigator || {}).userAgent
            , e = void 0 === s ? "" : s
            , o = l
            , V = h
            , t = z
            , M = m
            , f = !!o.document
            , H = !!V.documentElement && !!V.head && "function" == typeof V.addEventListener && "function" == typeof V.createElement
            , p = ~e.indexOf("MSIE") || ~e.indexOf("Trident/")
            , i = "___FONT_AWESOME___"
            , b = 16
            , C = "fa"
            , L = "svg-inline--fa"
            , B = "data-fa-i2svg"
            , u = "data-fa-pseudo-element"
            , d = "data-fa-pseudo-element-pending"
            , g = "data-prefix"
            , S = "data-icon"
            , A = "fontawesome-i2svg"
            , y = "async"
            , w = ["HTML", "HEAD", "STYLE", "SCRIPT"]
            , k = function () {
                try {
                    return !0
                } catch (c) {
                    return !1
                }
            }()
            , x = {
                fas: "solid",
                far: "regular",
                fal: "light",
                fad: "duotone",
                fab: "brands",
                fa: "solid"
            }
            , Z = {
                solid: "fas",
                regular: "far",
                light: "fal",
                duotone: "fad",
                brands: "fab"
            }
            , q = "fa-layers-text"
            , O = /Font Awesome 5 (Solid|Regular|Light|Duotone|Brands|Free|Pro)/
            , j = {
                900: "fas",
                400: "far",
                normal: "far",
                300: "fal"
            }
            , P = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            , E = P.concat([11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
            , N = ["class", "data-prefix", "data-icon", "data-fa-transform", "data-fa-mask"]
            , _ = {
                GROUP: "group",
                SWAP_OPACITY: "swap-opacity",
                PRIMARY: "primary",
                SECONDARY: "secondary"
            }
            , R = ["xs", "sm", "lg", "fw", "ul", "li", "border", "pull-left", "pull-right", "spin", "pulse", "rotate-90", "rotate-180", "rotate-270", "flip-horizontal", "flip-vertical", "flip-both", "stack", "stack-1x", "stack-2x", "inverse", "layers", "layers-text", "layers-counter", _.GROUP, _.SWAP_OPACITY, _.PRIMARY, _.SECONDARY].concat(P.map(function (c) {
                return "".concat(c, "x")
            })).concat(E.map(function (c) {
                return "w-".concat(c)
            }))
            , T = o.FontAwesomeConfig || {};
        if (V && "function" == typeof V.querySelector) {
            [["data-family-prefix", "familyPrefix"], ["data-replacement-class", "replacementClass"], ["data-auto-replace-svg", "autoReplaceSvg"], ["data-auto-add-css", "autoAddCss"], ["data-auto-a11y", "autoA11y"], ["data-search-pseudo-elements", "searchPseudoElements"], ["data-observe-mutations", "observeMutations"], ["data-mutate-approach", "mutateApproach"], ["data-keep-original-source", "keepOriginalSource"], ["data-measure-performance", "measurePerformance"], ["data-show-missing-icons", "showMissingIcons"]].forEach(function (c) {
                var l, h = r(c, 2), z = h[0], v = h[1], a = "" === (l = function (c) {
                    var l = V.querySelector("script[" + c + "]");
                    if (l)
                        return l.getAttribute(c)
                }(z)) || "false" !== l && ("true" === l || l);
                null != a && (T[v] = a)
            })
        }
        var F = X({}, {
            familyPrefix: C,
            replacementClass: L,
            autoReplaceSvg: !0,
            autoAddCss: !0,
            autoA11y: !0,
            searchPseudoElements: !1,
            observeMutations: !0,
            mutateApproach: "async",
            keepOriginalSource: !0,
            measurePerformance: !1,
            showMissingIcons: !0
        }, T);
        F.autoReplaceSvg || (F.observeMutations = !1);
        var K = X({}, F);
        o.FontAwesomeConfig = K;
        var I = o || {};
        I[i] || (I[i] = {}),
            I[i].styles || (I[i].styles = {}),
            I[i].hooks || (I[i].hooks = {}),
            I[i].shims || (I[i].shims = []);
        var Y = I[i]
            , D = []
            , W = !1;
        function U(c) {
            H && (W ? setTimeout(c, 0) : D.push(c))
        }
        H && ((W = (V.documentElement.doScroll ? /^loaded|^c/ : /^loaded|^i|^c/).test(V.readyState)) || V.addEventListener("DOMContentLoaded", function c() {
            V.removeEventListener("DOMContentLoaded", c),
                W = 1,
                D.map(function (c) {
                    return c()
                })
        }));
        var Q, G = "pending", J = "settled", $ = "fulfilled", cc = "rejected", lc = function () { }, hc = "undefined" != typeof global && void 0 !== global.process && "function" == typeof global.process.emit, zc = "undefined" == typeof setImmediate ? setTimeout : setImmediate, vc = [];
        function ac() {
            for (var c = 0; c < vc.length; c++)
                vc[c][0](vc[c][1]);
            Q = !(vc = [])
        }
        function mc(c, l) {
            vc.push([c, l]),
                Q || (Q = !0,
                    zc(ac, 0))
        }
        function sc(c) {
            var l = c.owner
                , h = l._state
                , z = l._data
                , v = c[h]
                , a = c.then;
            if ("function" == typeof v) {
                h = $;
                try {
                    z = v(z)
                } catch (c) {
                    fc(a, c)
                }
            }
            ec(a, z) || (h === $ && tc(a, z),
                h === cc && fc(a, z))
        }
        function ec(l, h) {
            var z;
            try {
                if (l === h)
                    throw new TypeError("A promises callback cannot return that same promise.");
                if (h && ("function" == typeof h || "object" === a(h))) {
                    var c = h.then;
                    if ("function" == typeof c)
                        return c.call(h, function (c) {
                            z || (z = !0,
                                h === c ? Mc(l, c) : tc(l, c))
                        }, function (c) {
                            z || (z = !0,
                                fc(l, c))
                        }),
                            !0
                }
            } catch (c) {
                return z || fc(l, c),
                    !0
            }
            return !1
        }
        function tc(c, l) {
            c !== l && ec(c, l) || Mc(c, l)
        }
        function Mc(c, l) {
            c._state === G && (c._state = J,
                c._data = l,
                mc(nc, c))
        }
        function fc(c, l) {
            c._state === G && (c._state = J,
                c._data = l,
                mc(Hc, c))
        }
        function rc(c) {
            c._then = c._then.forEach(sc)
        }
        function nc(c) {
            c._state = $,
                rc(c)
        }
        function Hc(c) {
            c._state = cc,
                rc(c),
                !c._handled && hc && global.process.emit("unhandledRejection", c._data, c)
        }
        function ic(c) {
            global.process.emit("rejectionHandled", c)
        }
        function oc(c) {
            if ("function" != typeof c)
                throw new TypeError("Promise resolver " + c + " is not a function");
            if (this instanceof oc == !1)
                throw new TypeError("Failed to construct 'Promise': Please use the 'new' operator, this object constructor cannot be called as a function.");
            this._then = [],
                function (c, l) {
                    function h(c) {
                        fc(l, c)
                    }
                    try {
                        c(function (c) {
                            tc(l, c)
                        }, h)
                    } catch (c) {
                        h(c)
                    }
                }(c, this)
        }
        oc.prototype = {
            constructor: oc,
            _state: G,
            _then: null,
            _data: void 0,
            _handled: !1,
            then: function (c, l) {
                var h = {
                    owner: this,
                    then: new this.constructor(lc),
                    fulfilled: c,
                    rejected: l
                };
                return !l && !c || this._handled || (this._handled = !0,
                    this._state === cc && hc && mc(ic, this)),
                    this._state === $ || this._state === cc ? mc(sc, h) : this._then.push(h),
                    h.then
            },
            catch: function (c) {
                return this.then(null, c)
            }
        },
            oc.all = function (s) {
                if (!Array.isArray(s))
                    throw new TypeError("You must pass an array to Promise.all().");
                return new oc(function (h, c) {
                    var z = []
                        , v = 0;
                    function l(l) {
                        return v++ ,
                            function (c) {
                                z[l] = c,
                                    --v || h(z)
                            }
                    }
                    for (var a, m = 0; m < s.length; m++)
                        (a = s[m]) && "function" == typeof a.then ? a.then(l(m), c) : z[m] = a;
                    v || h(z)
                }
                )
            }
            ,
            oc.race = function (v) {
                if (!Array.isArray(v))
                    throw new TypeError("You must pass an array to Promise.race().");
                return new oc(function (c, l) {
                    for (var h, z = 0; z < v.length; z++)
                        (h = v[z]) && "function" == typeof h.then ? h.then(c, l) : c(h)
                }
                )
            }
            ,
            oc.resolve = function (l) {
                return l && "object" === a(l) && l.constructor === oc ? l : new oc(function (c) {
                    c(l)
                }
                )
            }
            ,
            oc.reject = function (h) {
                return new oc(function (c, l) {
                    l(h)
                }
                )
            }
            ;
        var Vc = "function" == typeof Promise ? Promise : oc
            , Cc = b
            , Lc = {
                size: 16,
                x: 0,
                y: 0,
                rotate: 0,
                flipX: !1,
                flipY: !1
            };
        function uc(c) {
            if (c && H) {
                var l = V.createElement("style");
                l.setAttribute("type", "text/css"),
                    l.innerHTML = c;
                for (var h = V.head.childNodes, z = null, v = h.length - 1; -1 < v; v--) {
                    var a = h[v]
                        , m = (a.tagName || "").toUpperCase();
                    -1 < ["STYLE", "LINK"].indexOf(m) && (z = a)
                }
                return V.head.insertBefore(l, z),
                    c
            }
        }
        var dc = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
        function pc() {
            for (var c = 12, l = ""; 0 < c--;)
                l += dc[62 * Math.random() | 0];
            return l
        }
        function bc(c) {
            for (var l = [], h = (c || []).length >>> 0; h--;)
                l[h] = c[h];
            return l
        }
        function gc(c) {
            return c.classList ? bc(c.classList) : (c.getAttribute("class") || "").split(" ").filter(function (c) {
                return c
            })
        }
        function Sc(c, l) {
            var h, z = l.split("-"), v = z[0], a = z.slice(1).join("-");
            return v !== c || "" === a || (h = a,
                ~R.indexOf(h)) ? null : a
        }
        function Ac(c) {
            return "".concat(c).replace(/&/g, "&amp;").replace(/"/g, "&quot;").replace(/'/g, "&#39;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
        }
        function yc(h) {
            return Object.keys(h || {}).reduce(function (c, l) {
                return c + "".concat(l, ": ").concat(h[l], ";")
            }, "")
        }
        function wc(c) {
            return c.size !== Lc.size || c.x !== Lc.x || c.y !== Lc.y || c.rotate !== Lc.rotate || c.flipX || c.flipY
        }
        function kc(c) {
            var l = c.transform
                , h = c.containerWidth
                , z = c.iconWidth
                , v = {
                    transform: "translate(".concat(h / 2, " 256)")
                }
                , a = "translate(".concat(32 * l.x, ", ").concat(32 * l.y, ") ")
                , m = "scale(".concat(l.size / 16 * (l.flipX ? -1 : 1), ", ").concat(l.size / 16 * (l.flipY ? -1 : 1), ") ")
                , s = "rotate(".concat(l.rotate, " 0 0)");
            return {
                outer: v,
                inner: {
                    transform: "".concat(a, " ").concat(m, " ").concat(s)
                },
                path: {
                    transform: "translate(".concat(z / 2 * -1, " -256)")
                }
            }
        }
        var xc = {
            x: 0,
            y: 0,
            width: "100%",
            height: "100%"
        };
        function Zc(c) {
            var l = !(1 < arguments.length && void 0 !== arguments[1]) || arguments[1];
            return c.attributes && (c.attributes.fill || l) && (c.attributes.fill = "black"),
                c
        }
        function qc(c) {
            var l = c.icons
                , h = l.main
                , z = l.mask
                , v = c.prefix
                , a = c.iconName
                , m = c.transform
                , s = c.symbol
                , e = c.title
                , t = c.extra
                , M = c.watchable
                , f = void 0 !== M && M
                , r = z.found ? z : h
                , n = r.width
                , H = r.height
                , i = "fa-w-".concat(Math.ceil(n / H * 16))
                , o = [K.replacementClass, a ? "".concat(K.familyPrefix, "-").concat(a) : "", i].filter(function (c) {
                    return -1 === t.classes.indexOf(c)
                }).concat(t.classes).join(" ")
                , V = {
                    children: [],
                    attributes: X({}, t.attributes, {
                        "data-prefix": v,
                        "data-icon": a,
                        class: o,
                        role: t.attributes.role || "img",
                        xmlns: "http://www.w3.org/2000/svg",
                        viewBox: "0 0 ".concat(n, " ").concat(H)
                    })
                };
            f && (V.attributes[B] = ""),
                e && V.children.push({
                    tag: "title",
                    attributes: {
                        id: V.attributes["aria-labelledby"] || "title-".concat(pc())
                    },
                    children: [e]
                });
            var C, L, u, d, p, b, g, S, A, y, w, k, x, Z, q, O, j, P, E, N, _, R, T, F, I, Y, D = X({}, V, {
                prefix: v,
                iconName: a,
                main: h,
                mask: z,
                transform: m,
                symbol: s,
                styles: t.styles
            }), W = z.found && h.found ? (u = (C = D).children,
                d = C.attributes,
                p = C.main,
                b = C.mask,
                g = C.transform,
                S = p.width,
                A = p.icon,
                y = b.width,
                w = b.icon,
                k = kc({
                    transform: g,
                    containerWidth: y,
                    iconWidth: S
                }),
                x = {
                    tag: "rect",
                    attributes: X({}, xc, {
                        fill: "white"
                    })
                },
                Z = A.children ? {
                    children: A.children.map(Zc)
                } : {},
                q = {
                    tag: "g",
                    attributes: X({}, k.inner),
                    children: [Zc(X({
                        tag: A.tag,
                        attributes: X({}, A.attributes, k.path)
                    }, Z))]
                },
                O = {
                    tag: "g",
                    attributes: X({}, k.outer),
                    children: [q]
                },
                j = "mask-".concat(pc()),
                P = "clip-".concat(pc()),
                E = {
                    tag: "mask",
                    attributes: X({}, xc, {
                        id: j,
                        maskUnits: "userSpaceOnUse",
                        maskContentUnits: "userSpaceOnUse"
                    }),
                    children: [x, O]
                },
                N = {
                    tag: "defs",
                    children: [{
                        tag: "clipPath",
                        attributes: {
                            id: P
                        },
                        children: (L = w,
                            "g" === L.tag ? L.children : [L])
                    }, E]
                },
                u.push(N, {
                    tag: "rect",
                    attributes: X({
                        fill: "currentColor",
                        "clip-path": "url(#".concat(P, ")"),
                        mask: "url(#".concat(j, ")")
                    }, xc)
                }),
            {
                children: u,
                attributes: d
            }) : function (c) {
                var l = c.children
                    , h = c.attributes
                    , z = c.main
                    , v = c.transform
                    , a = yc(c.styles);
                if (0 < a.length && (h.style = a),
                    wc(v)) {
                    var m = kc({
                        transform: v,
                        containerWidth: z.width,
                        iconWidth: z.width
                    });
                    l.push({
                        tag: "g",
                        attributes: X({}, m.outer),
                        children: [{
                            tag: "g",
                            attributes: X({}, m.inner),
                            children: [{
                                tag: z.icon.tag,
                                children: z.icon.children,
                                attributes: X({}, z.icon.attributes, m.path)
                            }]
                        }]
                    })
                } else
                    l.push(z.icon);
                return {
                    children: l,
                    attributes: h
                }
            }(D), U = W.children, Q = W.attributes;
            return D.children = U,
                D.attributes = Q,
                s ? (R = (_ = D).prefix,
                    T = _.iconName,
                    F = _.children,
                    I = _.attributes,
                    Y = _.symbol,
                    [{
                        tag: "svg",
                        attributes: {
                            style: "display: none;"
                        },
                        children: [{
                            tag: "symbol",
                            attributes: X({}, I, {
                                id: !0 === Y ? "".concat(R, "-").concat(K.familyPrefix, "-").concat(T) : Y
                            }),
                            children: F
                        }]
                    }]) : function (c) {
                        var l = c.children
                            , h = c.main
                            , z = c.mask
                            , v = c.attributes
                            , a = c.styles
                            , m = c.transform;
                        if (wc(m) && h.found && !z.found) {
                            var s = h.width / h.height / 2
                                , e = .5;
                            v.style = yc(X({}, a, {
                                "transform-origin": "".concat(s + m.x / 16, "em ").concat(e + m.y / 16, "em")
                            }))
                        }
                        return [{
                            tag: "svg",
                            attributes: v,
                            children: l
                        }]
                    }(D)
        }
        function Oc(c) {
            var l = c.content
                , h = c.width
                , z = c.height
                , v = c.transform
                , a = c.title
                , m = c.extra
                , s = c.watchable
                , e = void 0 !== s && s
                , t = X({}, m.attributes, a ? {
                    title: a
                } : {}, {
                    class: m.classes.join(" ")
                });
            e && (t[B] = "");
            var M, f, r, n, H, i, o, V, C, L = X({}, m.styles);
            wc(v) && (L.transform = (f = (M = {
                transform: v,
                startCentered: !0,
                width: h,
                height: z
            }).transform,
                r = M.width,
                n = void 0 === r ? b : r,
                H = M.height,
                i = void 0 === H ? b : H,
                o = M.startCentered,
                C = "",
                C += (V = void 0 !== o && o) && p ? "translate(".concat(f.x / Cc - n / 2, "em, ").concat(f.y / Cc - i / 2, "em) ") : V ? "translate(calc(-50% + ".concat(f.x / Cc, "em), calc(-50% + ").concat(f.y / Cc, "em)) ") : "translate(".concat(f.x / Cc, "em, ").concat(f.y / Cc, "em) "),
                C += "scale(".concat(f.size / Cc * (f.flipX ? -1 : 1), ", ").concat(f.size / Cc * (f.flipY ? -1 : 1), ") "),
                C += "rotate(".concat(f.rotate, "deg) ")),
                L["-webkit-transform"] = L.transform);
            var u = yc(L);
            0 < u.length && (t.style = u);
            var d = [];
            return d.push({
                tag: "span",
                attributes: t,
                children: [l]
            }),
                a && d.push({
                    tag: "span",
                    attributes: {
                        class: "sr-only"
                    },
                    children: [a]
                }),
                d
        }
        var jc = function () { }
            , Pc = K.measurePerformance && M && M.mark && M.measure ? M : {
                mark: jc,
                measure: jc
            }
            , Ec = 'FA "5.12.0"'
            , Nc = function (c) {
                Pc.mark("".concat(Ec, " ").concat(c, " ends")),
                    Pc.measure("".concat(Ec, " ").concat(c), "".concat(Ec, " ").concat(c, " begins"), "".concat(Ec, " ").concat(c, " ends"))
            }
            , _c = {
                begin: function (c) {
                    return Pc.mark("".concat(Ec, " ").concat(c, " begins")),
                        function () {
                            return Nc(c)
                        }
                },
                end: Nc
            }
            , Rc = function (c, l, h, z) {
                var v, a, m, s, e, t = Object.keys(c), M = t.length, f = void 0 !== z ? (s = l,
                    e = z,
                    function (c, l, h, z) {
                        return s.call(e, c, l, h, z)
                    }
                ) : l;
                for (m = void 0 === h ? (v = 1,
                    c[t[0]]) : (v = 0,
                        h); v < M; v++)
                    m = f(m, c[a = t[v]], a, c);
                return m
            };
        function Tc(c) {
            for (var l = "", h = 0; h < c.length; h++) {
                l += ("000" + c.charCodeAt(h).toString(16)).slice(-4)
            }
            return l
        }
        var Fc = Y.styles
            , Ic = Y.shims
            , Yc = {}
            , Dc = {}
            , Wc = {}
            , Uc = function () {
                var c = function (z) {
                    return Rc(Fc, function (c, l, h) {
                        return c[h] = Rc(l, z, {}),
                            c
                    }, {})
                };
                Yc = c(function (c, l, h) {
                    return l[3] && (c[l[3]] = h),
                        c
                }),
                    Dc = c(function (l, c, h) {
                        var z = c[2];
                        return l[h] = h,
                            z.forEach(function (c) {
                                l[c] = h
                            }),
                            l
                    });
                var a = "far" in Fc;
                Wc = Rc(Ic, function (c, l) {
                    var h = l[0]
                        , z = l[1]
                        , v = l[2];
                    return "far" !== z || a || (z = "fas"),
                        c[h] = {
                            prefix: z,
                            iconName: v
                        },
                        c
                }, {})
            };
        function Qc(c, l) {
            return (Yc[c] || {})[l]
        }
        Uc();
        var Xc = Y.styles
            , Bc = function () {
                return {
                    prefix: null,
                    iconName: null,
                    rest: []
                }
            };
        function Kc(c) {
            return c.reduce(function (c, l) {
                var h = Sc(K.familyPrefix, l);
                if (Xc[l])
                    c.prefix = l;
                else if (K.autoFetchSvg && -1 < ["fas", "far", "fal", "fad", "fab", "fa"].indexOf(l))
                    c.prefix = l;
                else if (h) {
                    var z = "fa" === c.prefix ? Wc[h] || {
                        prefix: null,
                        iconName: null
                    } : {};
                    c.iconName = z.iconName || h,
                        c.prefix = z.prefix || c.prefix
                } else
                    l !== K.replacementClass && 0 !== l.indexOf("fa-w-") && c.rest.push(l);
                return c
            }, Bc())
        }
        function Gc(c, l, h) {
            if (c && c[l] && c[l][h])
                return {
                    prefix: l,
                    iconName: h,
                    icon: c[l][h]
                }
        }
        function Jc(c) {
            var h, l = c.tag, z = c.attributes, v = void 0 === z ? {} : z, a = c.children, m = void 0 === a ? [] : a;
            return "string" == typeof c ? Ac(c) : "<".concat(l, " ").concat((h = v,
                Object.keys(h || {}).reduce(function (c, l) {
                    return c + "".concat(l, '="').concat(Ac(h[l]), '" ')
                }, "").trim()), ">").concat(m.map(Jc).join(""), "</").concat(l, ">")
        }
        var $c = function () { };
        function cl(c) {
            return "string" == typeof (c.getAttribute ? c.getAttribute(B) : null)
        }
        var ll = {
            replace: function (c) {
                var l = c[0]
                    , h = c[1].map(function (c) {
                        return Jc(c)
                    }).join("\n");
                if (l.parentNode && l.outerHTML)
                    l.outerHTML = h + (K.keepOriginalSource && "svg" !== l.tagName.toLowerCase() ? "\x3c!-- ".concat(l.outerHTML, " --\x3e") : "");
                else if (l.parentNode) {
                    var z = document.createElement("span");
                    l.parentNode.replaceChild(z, l),
                        z.outerHTML = h
                }
            },
            nest: function (c) {
                var l = c[0]
                    , h = c[1];
                if (~gc(l).indexOf(K.replacementClass))
                    return ll.replace(c);
                var z = new RegExp("".concat(K.familyPrefix, "-.*"));
                delete h[0].attributes.style,
                    delete h[0].attributes.id;
                var v = h[0].attributes.class.split(" ").reduce(function (c, l) {
                    return l === K.replacementClass || l.match(z) ? c.toSvg.push(l) : c.toNode.push(l),
                        c
                }, {
                    toNode: [],
                    toSvg: []
                });
                h[0].attributes.class = v.toSvg.join(" ");
                var a = h.map(function (c) {
                    return Jc(c)
                }).join("\n");
                l.setAttribute("class", v.toNode.join(" ")),
                    l.setAttribute(B, ""),
                    l.innerHTML = a
            }
        };
        function hl(c) {
            c()
        }
        function zl(h, c) {
            var z = "function" == typeof c ? c : $c;
            if (0 === h.length)
                z();
            else {
                var l = hl;
                K.mutateApproach === y && (l = o.requestAnimationFrame || hl),
                    l(function () {
                        var c = !0 === K.autoReplaceSvg ? ll.replace : ll[K.autoReplaceSvg] || ll.replace
                            , l = _c.begin("mutate");
                        h.map(c),
                            l(),
                            z()
                    })
            }
        }
        var vl = !1;
        function al() {
            vl = !1
        }
        var ml = null;
        function sl(c) {
            if (t && K.observeMutations) {
                var v = c.treeCallback
                    , a = c.nodeCallback
                    , m = c.pseudoElementsCallback
                    , l = c.observeMutationsRoot
                    , h = void 0 === l ? V : l;
                ml = new t(function (c) {
                    vl || bc(c).forEach(function (c) {
                        if ("childList" === c.type && 0 < c.addedNodes.length && !cl(c.addedNodes[0]) && (K.searchPseudoElements && m(c.target),
                            v(c.target)),
                            "attributes" === c.type && c.target.parentNode && K.searchPseudoElements && m(c.target.parentNode),
                            "attributes" === c.type && cl(c.target) && ~N.indexOf(c.attributeName))
                            if ("class" === c.attributeName) {
                                var l = Kc(gc(c.target))
                                    , h = l.prefix
                                    , z = l.iconName;
                                h && c.target.setAttribute("data-prefix", h),
                                    z && c.target.setAttribute("data-icon", z)
                            } else
                                a(c.target)
                    })
                }
                ),
                    H && ml.observe(h, {
                        childList: !0,
                        attributes: !0,
                        characterData: !0,
                        subtree: !0
                    })
            }
        }
        function el(c) {
            var l, h, z = c.getAttribute("data-prefix"), v = c.getAttribute("data-icon"), a = void 0 !== c.innerText ? c.innerText.trim() : "", m = Kc(gc(c));
            return z && v && (m.prefix = z,
                m.iconName = v),
                m.prefix && 1 < a.length ? m.iconName = (l = m.prefix,
                    h = c.innerText,
                    (Dc[l] || {})[h]) : m.prefix && 1 === a.length && (m.iconName = Qc(m.prefix, Tc(c.innerText))),
                m
        }
        var tl = function (c) {
            var l = {
                size: 16,
                x: 0,
                y: 0,
                flipX: !1,
                flipY: !1,
                rotate: 0
            };
            return c ? c.toLowerCase().split(" ").reduce(function (c, l) {
                var h = l.toLowerCase().split("-")
                    , z = h[0]
                    , v = h.slice(1).join("-");
                if (z && "h" === v)
                    return c.flipX = !0,
                        c;
                if (z && "v" === v)
                    return c.flipY = !0,
                        c;
                if (v = parseFloat(v),
                    isNaN(v))
                    return c;
                switch (z) {
                    case "grow":
                        c.size = c.size + v;
                        break;
                    case "shrink":
                        c.size = c.size - v;
                        break;
                    case "left":
                        c.x = c.x - v;
                        break;
                    case "right":
                        c.x = c.x + v;
                        break;
                    case "up":
                        c.y = c.y - v;
                        break;
                    case "down":
                        c.y = c.y + v;
                        break;
                    case "rotate":
                        c.rotate = c.rotate + v
                }
                return c
            }, l) : l
        };
        function Ml(c) {
            var l, h, z, v, a, m, s, e = el(c), t = e.iconName, M = e.prefix, f = e.rest, r = (l = c.getAttribute("style"),
                h = [],
                l && (h = l.split(";").reduce(function (c, l) {
                    var h = l.split(":")
                        , z = h[0]
                        , v = h.slice(1);
                    return z && 0 < v.length && (c[z] = v.join(":").trim()),
                        c
                }, {})),
                h), n = tl(c.getAttribute("data-fa-transform")), H = null !== (z = c.getAttribute("data-fa-symbol")) && ("" === z || z), i = (a = bc((v = c).attributes).reduce(function (c, l) {
                    return "class" !== c.name && "style" !== c.name && (c[l.name] = l.value),
                        c
                }, {}),
                    m = v.getAttribute("title"),
                    K.autoA11y && (m ? a["aria-labelledby"] = "".concat(K.replacementClass, "-title-").concat(pc()) : (a["aria-hidden"] = "true",
                        a.focusable = "false")),
                    a), o = (s = c.getAttribute("data-fa-mask")) ? Kc(s.split(" ").map(function (c) {
                        return c.trim()
                    })) : Bc();
            return {
                iconName: t,
                title: c.getAttribute("title"),
                prefix: M,
                transform: n,
                symbol: H,
                mask: o,
                extra: {
                    classes: f,
                    styles: r,
                    attributes: i
                }
            }
        }
        function fl(c) {
            this.name = "MissingIcon",
                this.message = c || "Icon unavailable",
                this.stack = (new Error).stack
        }
        (fl.prototype = Object.create(Error.prototype)).constructor = fl;
        var rl = {
            fill: "currentColor"
        }
            , nl = {
                attributeType: "XML",
                repeatCount: "indefinite",
                dur: "2s"
            }
            , Hl = {
                tag: "path",
                attributes: X({}, rl, {
                    d: "M156.5,447.7l-12.6,29.5c-18.7-9.5-35.9-21.2-51.5-34.9l22.7-22.7C127.6,430.5,141.5,440,156.5,447.7z M40.6,272H8.5 c1.4,21.2,5.4,41.7,11.7,61.1L50,321.2C45.1,305.5,41.8,289,40.6,272z M40.6,240c1.4-18.8,5.2-37,11.1-54.1l-29.5-12.6 C14.7,194.3,10,216.7,8.5,240H40.6z M64.3,156.5c7.8-14.9,17.2-28.8,28.1-41.5L69.7,92.3c-13.7,15.6-25.5,32.8-34.9,51.5 L64.3,156.5z M397,419.6c-13.9,12-29.4,22.3-46.1,30.4l11.9,29.8c20.7-9.9,39.8-22.6,56.9-37.6L397,419.6z M115,92.4 c13.9-12,29.4-22.3,46.1-30.4l-11.9-29.8c-20.7,9.9-39.8,22.6-56.8,37.6L115,92.4z M447.7,355.5c-7.8,14.9-17.2,28.8-28.1,41.5 l22.7,22.7c13.7-15.6,25.5-32.9,34.9-51.5L447.7,355.5z M471.4,272c-1.4,18.8-5.2,37-11.1,54.1l29.5,12.6 c7.5-21.1,12.2-43.5,13.6-66.8H471.4z M321.2,462c-15.7,5-32.2,8.2-49.2,9.4v32.1c21.2-1.4,41.7-5.4,61.1-11.7L321.2,462z M240,471.4c-18.8-1.4-37-5.2-54.1-11.1l-12.6,29.5c21.1,7.5,43.5,12.2,66.8,13.6V471.4z M462,190.8c5,15.7,8.2,32.2,9.4,49.2h32.1 c-1.4-21.2-5.4-41.7-11.7-61.1L462,190.8z M92.4,397c-12-13.9-22.3-29.4-30.4-46.1l-29.8,11.9c9.9,20.7,22.6,39.8,37.6,56.9 L92.4,397z M272,40.6c18.8,1.4,36.9,5.2,54.1,11.1l12.6-29.5C317.7,14.7,295.3,10,272,8.5V40.6z M190.8,50 c15.7-5,32.2-8.2,49.2-9.4V8.5c-21.2,1.4-41.7,5.4-61.1,11.7L190.8,50z M442.3,92.3L419.6,115c12,13.9,22.3,29.4,30.5,46.1 l29.8-11.9C470,128.5,457.3,109.4,442.3,92.3z M397,92.4l22.7-22.7c-15.6-13.7-32.8-25.5-51.5-34.9l-12.6,29.5 C370.4,72.1,384.4,81.5,397,92.4z"
                })
            }
            , il = X({}, nl, {
                attributeName: "opacity"
            })
            , ol = {
                tag: "g",
                children: [Hl, {
                    tag: "circle",
                    attributes: X({}, rl, {
                        cx: "256",
                        cy: "364",
                        r: "28"
                    }),
                    children: [{
                        tag: "animate",
                        attributes: X({}, nl, {
                            attributeName: "r",
                            values: "28;14;28;28;14;28;"
                        })
                    }, {
                        tag: "animate",
                        attributes: X({}, il, {
                            values: "1;0;1;1;0;1;"
                        })
                    }]
                }, {
                        tag: "path",
                        attributes: X({}, rl, {
                            opacity: "1",
                            d: "M263.7,312h-16c-6.6,0-12-5.4-12-12c0-71,77.4-63.9,77.4-107.8c0-20-17.8-40.2-57.4-40.2c-29.1,0-44.3,9.6-59.2,28.7 c-3.9,5-11.1,6-16.2,2.4l-13.1-9.2c-5.6-3.9-6.9-11.8-2.6-17.2c21.2-27.2,46.4-44.7,91.2-44.7c52.3,0,97.4,29.8,97.4,80.2 c0,67.6-77.4,63.5-77.4,107.8C275.7,306.6,270.3,312,263.7,312z"
                        }),
                        children: [{
                            tag: "animate",
                            attributes: X({}, il, {
                                values: "1;0;0;0;0;1;"
                            })
                        }]
                    }, {
                        tag: "path",
                        attributes: X({}, rl, {
                            opacity: "0",
                            d: "M232.5,134.5l7,168c0.3,6.4,5.6,11.5,12,11.5h9c6.4,0,11.7-5.1,12-11.5l7-168c0.3-6.8-5.2-12.5-12-12.5h-23 C237.7,122,232.2,127.7,232.5,134.5z"
                        }),
                        children: [{
                            tag: "animate",
                            attributes: X({}, il, {
                                values: "0;0;1;1;0;0;"
                            })
                        }]
                    }]
            }
            , Vl = Y.styles;
        function Cl(c) {
            var l = c[0]
                , h = c[1]
                , z = r(c.slice(4), 1)[0];
            return {
                found: !0,
                width: l,
                height: h,
                icon: Array.isArray(z) ? {
                    tag: "g",
                    attributes: {
                        class: "".concat(K.familyPrefix, "-").concat(_.GROUP)
                    },
                    children: [{
                        tag: "path",
                        attributes: {
                            class: "".concat(K.familyPrefix, "-").concat(_.SECONDARY),
                            fill: "currentColor",
                            d: z[0]
                        }
                    }, {
                        tag: "path",
                        attributes: {
                            class: "".concat(K.familyPrefix, "-").concat(_.PRIMARY),
                            fill: "currentColor",
                            d: z[1]
                        }
                    }]
                } : {
                        tag: "path",
                        attributes: {
                            fill: "currentColor",
                            d: z
                        }
                    }
            }
        }
        function Ll(z, v) {
            return new Vc(function (c, l) {
                var h = {
                    found: !1,
                    width: 512,
                    height: 512,
                    icon: ol
                };
                if (z && v && Vl[v] && Vl[v][z])
                    return c(Cl(Vl[v][z]));
                "object" === a(o.FontAwesomeKitConfig) && "string" == typeof window.FontAwesomeKitConfig.token && o.FontAwesomeKitConfig.token,
                    z && v && !K.showMissingIcons ? l(new fl("Icon is missing for prefix ".concat(v, " with icon name ").concat(z))) : c(h)
            }
            )
        }
        var ul = Y.styles;
        function dl(c) {
            var a, l, m, s, e, t, M, h, f, z = Ml(c);
            return ~z.extra.classes.indexOf(q) ? function (c, l) {
                var h = l.title
                    , z = l.transform
                    , v = l.extra
                    , a = null
                    , m = null;
                if (p) {
                    var s = parseInt(getComputedStyle(c).fontSize, 10)
                        , e = c.getBoundingClientRect();
                    a = e.width / s,
                        m = e.height / s
                }
                return K.autoA11y && !h && (v.attributes["aria-hidden"] = "true"),
                    Vc.resolve([c, Oc({
                        content: c.innerHTML,
                        width: a,
                        height: m,
                        transform: z,
                        title: h,
                        extra: v,
                        watchable: !0
                    })])
            }(c, z) : (a = c,
                m = (l = z).iconName,
                s = l.title,
                e = l.prefix,
                t = l.transform,
                M = l.symbol,
                h = l.mask,
                f = l.extra,
                new Vc(function (v, c) {
                    Vc.all([Ll(m, e), Ll(h.iconName, h.prefix)]).then(function (c) {
                        var l = r(c, 2)
                            , h = l[0]
                            , z = l[1];
                        v([a, qc({
                            icons: {
                                main: h,
                                mask: z
                            },
                            prefix: e,
                            iconName: m,
                            transform: t,
                            symbol: M,
                            mask: z,
                            title: s,
                            extra: f,
                            watchable: !0
                        })])
                    })
                }
                ))
        }
        function pl(c) {
            var h = 1 < arguments.length && void 0 !== arguments[1] ? arguments[1] : null;
            if (H) {
                var l = V.documentElement.classList
                    , z = function (c) {
                        return l.add("".concat(A, "-").concat(c))
                    }
                    , v = function (c) {
                        return l.remove("".concat(A, "-").concat(c))
                    }
                    , a = K.autoFetchSvg ? Object.keys(x) : Object.keys(ul)
                    , m = [".".concat(q, ":not([").concat(B, "])")].concat(a.map(function (c) {
                        return ".".concat(c, ":not([").concat(B, "])")
                    })).join(", ");
                if (0 !== m.length) {
                    var s = [];
                    try {
                        s = bc(c.querySelectorAll(m))
                    } catch (c) { }
                    if (0 < s.length) {
                        z("pending"),
                            v("complete");
                        var e = _c.begin("onTree")
                            , t = s.reduce(function (c, l) {
                                try {
                                    var h = dl(l);
                                    h && c.push(h)
                                } catch (c) {
                                    k || c instanceof fl && console.error(c)
                                }
                                return c
                            }, []);
                        return new Vc(function (l, c) {
                            Vc.all(t).then(function (c) {
                                zl(c, function () {
                                    z("active"),
                                        z("complete"),
                                        v("pending"),
                                        "function" == typeof h && h(),
                                        e(),
                                        l()
                                })
                            }).catch(function () {
                                e(),
                                    c()
                            })
                        }
                        )
                    }
                }
            }
        }
        function bl(c) {
            var l = 1 < arguments.length && void 0 !== arguments[1] ? arguments[1] : null;
            dl(c).then(function (c) {
                c && zl([c], l)
            })
        }
        function gl(n, H) {
            var i = "".concat(d).concat(H.replace(":", "-"));
            return new Vc(function (z, c) {
                if (null !== n.getAttribute(i))
                    return z();
                var l = bc(n.children).filter(function (c) {
                    return c.getAttribute(u) === H
                })[0]
                    , h = o.getComputedStyle(n, H)
                    , v = h.getPropertyValue("font-family").match(O)
                    , a = h.getPropertyValue("font-weight");
                if (l && !v)
                    return n.removeChild(l),
                        z();
                if (v) {
                    var m = h.getPropertyValue("content")
                        , s = ~["Solid", "Regular", "Light", "Duotone", "Brands"].indexOf(v[1]) ? Z[v[1].toLowerCase()] : j[a]
                        , e = Tc(3 === m.length ? m.substr(1, 1) : m)
                        , t = Qc(s, e)
                        , M = t;
                    if (!t || l && l.getAttribute(g) === s && l.getAttribute(S) === M)
                        z();
                    else {
                        n.setAttribute(i, M),
                            l && n.removeChild(l);
                        var f = {
                            iconName: null,
                            title: null,
                            prefix: null,
                            transform: Lc,
                            symbol: !1,
                            mask: null,
                            extra: {
                                classes: [],
                                styles: {},
                                attributes: {}
                            }
                        }
                            , r = f.extra;
                        r.attributes[u] = H,
                            Ll(t, s).then(function (c) {
                                var l = qc(X({}, f, {
                                    icons: {
                                        main: c,
                                        mask: Bc()
                                    },
                                    prefix: s,
                                    iconName: M,
                                    extra: r,
                                    watchable: !0
                                }))
                                    , h = V.createElement("svg");
                                ":before" === H ? n.insertBefore(h, n.firstChild) : n.appendChild(h),
                                    h.outerHTML = l.map(function (c) {
                                        return Jc(c)
                                    }).join("\n"),
                                    n.removeAttribute(i),
                                    z()
                            }).catch(c)
                    }
                } else
                    z()
            }
            )
        }
        function Sl(c) {
            return Vc.all([gl(c, ":before"), gl(c, ":after")])
        }
        function Al(c) {
            return !(c.parentNode === document.head || ~w.indexOf(c.tagName.toUpperCase()) || c.getAttribute(u) || c.parentNode && "svg" === c.parentNode.tagName)
        }
        function yl(v) {
            if (H)
                return new Vc(function (c, l) {
                    var h = bc(v.querySelectorAll("*")).filter(Al).map(Sl)
                        , z = _c.begin("searchPseudoElements");
                    vl = !0,
                        Vc.all(h).then(function () {
                            z(),
                                al(),
                                c()
                        }).catch(function () {
                            z(),
                                al(),
                                l()
                        })
                }
                )
        }
        var wl = "svg:not(:root).svg-inline--fa{overflow:visible}.svg-inline--fa{display:inline-block;font-size:inherit;height:1em;overflow:visible;vertical-align:-.125em}.svg-inline--fa.fa-lg{vertical-align:-.225em}.svg-inline--fa.fa-w-1{width:.0625em}.svg-inline--fa.fa-w-2{width:.125em}.svg-inline--fa.fa-w-3{width:.1875em}.svg-inline--fa.fa-w-4{width:.25em}.svg-inline--fa.fa-w-5{width:.3125em}.svg-inline--fa.fa-w-6{width:.375em}.svg-inline--fa.fa-w-7{width:.4375em}.svg-inline--fa.fa-w-8{width:.5em}.svg-inline--fa.fa-w-9{width:.5625em}.svg-inline--fa.fa-w-10{width:.625em}.svg-inline--fa.fa-w-11{width:.6875em}.svg-inline--fa.fa-w-12{width:.75em}.svg-inline--fa.fa-w-13{width:.8125em}.svg-inline--fa.fa-w-14{width:.875em}.svg-inline--fa.fa-w-15{width:.9375em}.svg-inline--fa.fa-w-16{width:1em}.svg-inline--fa.fa-w-17{width:1.0625em}.svg-inline--fa.fa-w-18{width:1.125em}.svg-inline--fa.fa-w-19{width:1.1875em}.svg-inline--fa.fa-w-20{width:1.25em}.svg-inline--fa.fa-pull-left{margin-right:.3em;width:auto}.svg-inline--fa.fa-pull-right{margin-left:.3em;width:auto}.svg-inline--fa.fa-border{height:1.5em}.svg-inline--fa.fa-li{width:2em}.svg-inline--fa.fa-fw{width:1.25em}.fa-layers svg.svg-inline--fa{bottom:0;left:0;margin:auto;position:absolute;right:0;top:0}.fa-layers{display:inline-block;height:1em;position:relative;text-align:center;vertical-align:-.125em;width:1em}.fa-layers svg.svg-inline--fa{-webkit-transform-origin:center center;transform-origin:center center}.fa-layers-counter,.fa-layers-text{display:inline-block;position:absolute;text-align:center}.fa-layers-text{left:50%;top:50%;-webkit-transform:translate(-50%,-50%);transform:translate(-50%,-50%);-webkit-transform-origin:center center;transform-origin:center center}.fa-layers-counter{background-color:#ff253a;border-radius:1em;-webkit-box-sizing:border-box;box-sizing:border-box;color:#fff;height:1.5em;line-height:1;max-width:5em;min-width:1.5em;overflow:hidden;padding:.25em;right:0;text-overflow:ellipsis;top:0;-webkit-transform:scale(.25);transform:scale(.25);-webkit-transform-origin:top right;transform-origin:top right}.fa-layers-bottom-right{bottom:0;right:0;top:auto;-webkit-transform:scale(.25);transform:scale(.25);-webkit-transform-origin:bottom right;transform-origin:bottom right}.fa-layers-bottom-left{bottom:0;left:0;right:auto;top:auto;-webkit-transform:scale(.25);transform:scale(.25);-webkit-transform-origin:bottom left;transform-origin:bottom left}.fa-layers-top-right{right:0;top:0;-webkit-transform:scale(.25);transform:scale(.25);-webkit-transform-origin:top right;transform-origin:top right}.fa-layers-top-left{left:0;right:auto;top:0;-webkit-transform:scale(.25);transform:scale(.25);-webkit-transform-origin:top left;transform-origin:top left}.fa-lg{font-size:1.3333333333em;line-height:.75em;vertical-align:-.0667em}.fa-xs{font-size:.75em}.fa-sm{font-size:.875em}.fa-1x{font-size:1em}.fa-2x{font-size:2em}.fa-3x{font-size:3em}.fa-4x{font-size:4em}.fa-5x{font-size:5em}.fa-6x{font-size:6em}.fa-7x{font-size:7em}.fa-8x{font-size:8em}.fa-9x{font-size:9em}.fa-10x{font-size:10em}.fa-fw{text-align:center;width:1.25em}.fa-ul{list-style-type:none;margin-left:2.5em;padding-left:0}.fa-ul>li{position:relative}.fa-li{left:-2em;position:absolute;text-align:center;width:2em;line-height:inherit}.fa-border{border:solid .08em #eee;border-radius:.1em;padding:.2em .25em .15em}.fa-pull-left{float:left}.fa-pull-right{float:right}.fa.fa-pull-left,.fab.fa-pull-left,.fal.fa-pull-left,.far.fa-pull-left,.fas.fa-pull-left{margin-right:.3em}.fa.fa-pull-right,.fab.fa-pull-right,.fal.fa-pull-right,.far.fa-pull-right,.fas.fa-pull-right{margin-left:.3em}.fa-spin{-webkit-animation:fa-spin 2s infinite linear;animation:fa-spin 2s infinite linear}.fa-pulse{-webkit-animation:fa-spin 1s infinite steps(8);animation:fa-spin 1s infinite steps(8)}@-webkit-keyframes fa-spin{0%{-webkit-transform:rotate(0);transform:rotate(0)}100%{-webkit-transform:rotate(360deg);transform:rotate(360deg)}}@keyframes fa-spin{0%{-webkit-transform:rotate(0);transform:rotate(0)}100%{-webkit-transform:rotate(360deg);transform:rotate(360deg)}}.fa-rotate-90{-webkit-transform:rotate(90deg);transform:rotate(90deg)}.fa-rotate-180{-webkit-transform:rotate(180deg);transform:rotate(180deg)}.fa-rotate-270{-webkit-transform:rotate(270deg);transform:rotate(270deg)}.fa-flip-horizontal{-webkit-transform:scale(-1,1);transform:scale(-1,1)}.fa-flip-vertical{-webkit-transform:scale(1,-1);transform:scale(1,-1)}.fa-flip-both,.fa-flip-horizontal.fa-flip-vertical{-webkit-transform:scale(-1,-1);transform:scale(-1,-1)}:root .fa-flip-both,:root .fa-flip-horizontal,:root .fa-flip-vertical,:root .fa-rotate-180,:root .fa-rotate-270,:root .fa-rotate-90{-webkit-filter:none;filter:none}.fa-stack{display:inline-block;height:2em;position:relative;width:2.5em}.fa-stack-1x,.fa-stack-2x{bottom:0;left:0;margin:auto;position:absolute;right:0;top:0}.svg-inline--fa.fa-stack-1x{height:1em;width:1.25em}.svg-inline--fa.fa-stack-2x{height:2em;width:2.5em}.fa-inverse{color:#fff}.sr-only{border:0;clip:rect(0,0,0,0);height:1px;margin:-1px;overflow:hidden;padding:0;position:absolute;width:1px}.sr-only-focusable:active,.sr-only-focusable:focus{clip:auto;height:auto;margin:0;overflow:visible;position:static;width:auto}.svg-inline--fa .fa-primary{fill:var(--fa-primary-color,currentColor);opacity:1;opacity:var(--fa-primary-opacity,1)}.svg-inline--fa .fa-secondary{fill:var(--fa-secondary-color,currentColor);opacity:.4;opacity:var(--fa-secondary-opacity,.4)}.svg-inline--fa.fa-swap-opacity .fa-primary{opacity:.4;opacity:var(--fa-secondary-opacity,.4)}.svg-inline--fa.fa-swap-opacity .fa-secondary{opacity:1;opacity:var(--fa-primary-opacity,1)}.svg-inline--fa mask .fa-primary,.svg-inline--fa mask .fa-secondary{fill:#000}.fad.fa-inverse{color:#fff}";
        function kl() {
            var c = C
                , l = L
                , h = K.familyPrefix
                , z = K.replacementClass
                , v = wl;
            if (h !== c || z !== l) {
                var a = new RegExp("\\.".concat(c, "\\-"), "g")
                    , m = new RegExp("\\--".concat(c, "\\-"), "g")
                    , s = new RegExp("\\.".concat(l), "g");
                v = v.replace(a, ".".concat(h, "-")).replace(m, "--".concat(h, "-")).replace(s, ".".concat(z))
            }
            return v
        }
        function xl() {
            K.autoAddCss && !Pl && (uc(kl()),
                Pl = !0)
        }
        function Zl(l, c) {
            return Object.defineProperty(l, "abstract", {
                get: c
            }),
                Object.defineProperty(l, "html", {
                    get: function () {
                        return l.abstract.map(function (c) {
                            return Jc(c)
                        })
                    }
                }),
                Object.defineProperty(l, "node", {
                    get: function () {
                        if (H) {
                            var c = V.createElement("div");
                            return c.innerHTML = l.html,
                                c.children
                        }
                    }
                }),
                l
        }
        function ql(c) {
            var l = c.prefix
                , h = void 0 === l ? "fa" : l
                , z = c.iconName;
            if (z)
                return Gc(jl.definitions, h, z) || Gc(Y.styles, h, z)
        }
        var Ol, jl = new (function () {
            function c() {
                !function (c, l) {
                    if (!(c instanceof l))
                        throw new TypeError("Cannot call a class as a function")
                }(this, c),
                    this.definitions = {}
            }
            var l, h, z;
            return l = c,
                (h = [{
                    key: "add",
                    value: function () {
                        for (var l = this, c = arguments.length, h = new Array(c), z = 0; z < c; z++)
                            h[z] = arguments[z];
                        var v = h.reduce(this._pullDefinitions, {});
                        Object.keys(v).forEach(function (c) {
                            l.definitions[c] = X({}, l.definitions[c] || {}, v[c]),
                                function c(l, z) {
                                    var h = (2 < arguments.length && void 0 !== arguments[2] ? arguments[2] : {}).skipHooks
                                        , v = void 0 !== h && h
                                        , a = Object.keys(z).reduce(function (c, l) {
                                            var h = z[l];
                                            return h.icon ? c[h.iconName] = h.icon : c[l] = h,
                                                c
                                        }, {});
                                    "function" != typeof Y.hooks.addPack || v ? Y.styles[l] = X({}, Y.styles[l] || {}, a) : Y.hooks.addPack(l, a),
                                        "fas" === l && c("fa", z)
                                }(c, v[c]),
                                Uc()
                        })
                    }
                }, {
                    key: "reset",
                    value: function () {
                        this.definitions = {}
                    }
                }, {
                    key: "_pullDefinitions",
                    value: function (a, c) {
                        var m = c.prefix && c.iconName && c.icon ? {
                            0: c
                        } : c;
                        return Object.keys(m).map(function (c) {
                            var l = m[c]
                                , h = l.prefix
                                , z = l.iconName
                                , v = l.icon;
                            a[h] || (a[h] = {}),
                                a[h][z] = v
                        }),
                            a
                    }
                }]) && v(l.prototype, h),
                z && v(l, z),
                c
        }()), Pl = !1, El = {
            i2svg: function () {
                var c = 0 < arguments.length && void 0 !== arguments[0] ? arguments[0] : {};
                if (H) {
                    xl();
                    var l = c.node
                        , h = void 0 === l ? V : l
                        , z = c.callback
                        , v = void 0 === z ? function () { }
                            : z;
                    return K.searchPseudoElements && yl(h),
                        pl(h, v)
                }
                return Vc.reject("Operation requires a DOM of some kind.")
            },
            css: kl,
            insertCss: function () {
                Pl || (uc(kl()),
                    Pl = !0)
            },
            watch: function () {
                var c = 0 < arguments.length && void 0 !== arguments[0] ? arguments[0] : {}
                    , l = c.autoReplaceSvgRoot
                    , h = c.observeMutationsRoot;
                !1 === K.autoReplaceSvg && (K.autoReplaceSvg = !0),
                    K.observeMutations = !0,
                    U(function () {
                        Rl({
                            autoReplaceSvgRoot: l
                        }),
                            sl({
                                treeCallback: pl,
                                nodeCallback: bl,
                                pseudoElementsCallback: yl,
                                observeMutationsRoot: h
                            })
                    })
            }
        }, Nl = (Ol = function (c) {
            var l = 1 < arguments.length && void 0 !== arguments[1] ? arguments[1] : {}
                , h = l.transform
                , z = void 0 === h ? Lc : h
                , v = l.symbol
                , a = void 0 !== v && v
                , m = l.mask
                , s = void 0 === m ? null : m
                , e = l.title
                , t = void 0 === e ? null : e
                , M = l.classes
                , f = void 0 === M ? [] : M
                , r = l.attributes
                , n = void 0 === r ? {} : r
                , H = l.styles
                , i = void 0 === H ? {} : H;
            if (c) {
                var o = c.prefix
                    , V = c.iconName
                    , C = c.icon;
                return Zl(X({
                    type: "icon"
                }, c), function () {
                    return xl(),
                        K.autoA11y && (t ? n["aria-labelledby"] = "".concat(K.replacementClass, "-title-").concat(pc()) : (n["aria-hidden"] = "true",
                            n.focusable = "false")),
                        qc({
                            icons: {
                                main: Cl(C),
                                mask: s ? Cl(s.icon) : {
                                    found: !1,
                                    width: null,
                                    height: null,
                                    icon: {}
                                }
                            },
                            prefix: o,
                            iconName: V,
                            transform: X({}, Lc, z),
                            symbol: a,
                            title: t,
                            extra: {
                                attributes: n,
                                styles: i,
                                classes: f
                            }
                        })
                })
            }
        }
            ,
            function (c) {
                var l = 1 < arguments.length && void 0 !== arguments[1] ? arguments[1] : {}
                    , h = (c || {}).icon ? c : ql(c || {})
                    , z = l.mask;
                return z && (z = (z || {}).icon ? z : ql(z || {})),
                    Ol(h, X({}, l, {
                        mask: z
                    }))
            }
        ), _l = {
            noAuto: function () {
                K.autoReplaceSvg = !1,
                    K.observeMutations = !1,
                    ml && ml.disconnect()
            },
            config: K,
            dom: El,
            library: jl,
            parse: {
                transform: function (c) {
                    return tl(c)
                }
            },
            findIconDefinition: ql,
            icon: Nl,
            text: function (c) {
                var l = 1 < arguments.length && void 0 !== arguments[1] ? arguments[1] : {}
                    , h = l.transform
                    , z = void 0 === h ? Lc : h
                    , v = l.title
                    , a = void 0 === v ? null : v
                    , m = l.classes
                    , s = void 0 === m ? [] : m
                    , e = l.attributes
                    , t = void 0 === e ? {} : e
                    , M = l.styles
                    , f = void 0 === M ? {} : M;
                return Zl({
                    type: "text",
                    content: c
                }, function () {
                    return xl(),
                        Oc({
                            content: c,
                            transform: X({}, Lc, z),
                            title: a,
                            extra: {
                                attributes: t,
                                styles: f,
                                classes: ["".concat(K.familyPrefix, "-layers-text")].concat(n(s))
                            }
                        })
                })
            },
            counter: function (c) {
                var l = 1 < arguments.length && void 0 !== arguments[1] ? arguments[1] : {}
                    , h = l.title
                    , z = void 0 === h ? null : h
                    , v = l.classes
                    , a = void 0 === v ? [] : v
                    , m = l.attributes
                    , s = void 0 === m ? {} : m
                    , e = l.styles
                    , t = void 0 === e ? {} : e;
                return Zl({
                    type: "counter",
                    content: c
                }, function () {
                    return xl(),
                        function (c) {
                            var l = c.content
                                , h = c.title
                                , z = c.extra
                                , v = X({}, z.attributes, h ? {
                                    title: h
                                } : {}, {
                                    class: z.classes.join(" ")
                                })
                                , a = yc(z.styles);
                            0 < a.length && (v.style = a);
                            var m = [];
                            return m.push({
                                tag: "span",
                                attributes: v,
                                children: [l]
                            }),
                                h && m.push({
                                    tag: "span",
                                    attributes: {
                                        class: "sr-only"
                                    },
                                    children: [h]
                                }),
                                m
                        }({
                            content: c.toString(),
                            title: z,
                            extra: {
                                attributes: s,
                                styles: t,
                                classes: ["".concat(K.familyPrefix, "-layers-counter")].concat(n(a))
                            }
                        })
                })
            },
            layer: function (c) {
                var l = (1 < arguments.length && void 0 !== arguments[1] ? arguments[1] : {}).classes
                    , h = void 0 === l ? [] : l;
                return Zl({
                    type: "layer"
                }, function () {
                    xl();
                    var l = [];
                    return c(function (c) {
                        Array.isArray(c) ? c.map(function (c) {
                            l = l.concat(c.abstract)
                        }) : l = l.concat(c.abstract)
                    }),
                        [{
                            tag: "span",
                            attributes: {
                                class: ["".concat(K.familyPrefix, "-layers")].concat(n(h)).join(" ")
                            },
                            children: l
                        }]
                })
            },
            toHtml: Jc
        }, Rl = function () {
            var c = (0 < arguments.length && void 0 !== arguments[0] ? arguments[0] : {}).autoReplaceSvgRoot
                , l = void 0 === c ? V : c;
            (0 < Object.keys(Y.styles).length || K.autoFetchSvg) && H && K.autoReplaceSvg && _l.dom.i2svg({
                node: l
            })
        };
        !function (c) {
            try {
                c()
            } catch (c) {
                if (!k)
                    throw c
            }
        }(function () {
            f && (o.FontAwesome || (o.FontAwesome = _l),
                U(function () {
                    Rl(),
                        sl({
                            treeCallback: pl,
                            nodeCallback: bl,
                            pseudoElementsCallback: yl
                        })
                })),
                Y.hooks = X({}, Y.hooks, {
                    addPack: function (c, l) {
                        Y.styles[c] = X({}, Y.styles[c] || {}, l),
                            Uc(),
                            Rl()
                    },
                    addShims: function (c) {
                        var l;
                        (l = Y.shims).push.apply(l, n(c)),
                            Uc(),
                            Rl()
                    }
                })
        })
    }();
