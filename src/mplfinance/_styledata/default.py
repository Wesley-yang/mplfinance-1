style = dict(style_name    = 'default',
             base_mpl_style= 'seaborn-darkgrid', 
             marketcolors  = {'candle'  : {'up':'w', 'down':'k'},
                              'edge'    : {'up':'k', 'down':'k'},
                              'wick'    : {'up':'k', 'down':'k'},
                              'ohlc'    : {'up':'k', 'down':'k'},
                              'volume'  : {'up':'#1f77b4', 'down':'#1f77b4'},
                              'vcedge'  : {'up':'#1f77b4', 'down':'#1f77b4'},
                              'vcdopcod': False, # Volume Color is Per Price Change On Day
                              'alpha'   : 0.9,
                             },
             mavcolors     = ['#40e0d0','#ff00ff','#ffd700','#1f77b4',
                              '#ff7f0e','#2ca02c','#e377c2'],
             y_on_right    = False,
             gridcolor     = None,
             gridstyle     = None,
             facecolor     = '#DCE3EF',
             rc            = [ ('axes.edgecolor'  , 'black'   ),
                               ('axes.linewidth'  ,  1.5      ),
                               ('axes.labelsize'  , 'large'   ),
                               ('axes.labelweight', 'semibold'),
                               ('lines.linewidth' ,  2.0      ),
                               ('font.weight'     , 'medium'  ),
                               ('font.size'       ,  12.0     ),
                               ('figure.titlesize', 'x-large' ),
                               ('figure.titleweight','semibold'),
                             ],
             base_mpf_style= 'default'
            )
