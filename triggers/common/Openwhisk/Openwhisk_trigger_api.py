 _ _ a u t h o r _ _   =   ' k o n g s e o k h w a n '  
  
 i m p o r t   j s o n  
 i m p o r t   r e q u e s t s  
 f r o m   o s l o _ l o g   i m p o r t   l o g   a s   l o g g i n g  
  
 L O G   =   l o g g i n g . g e t L o g g e r ( _ _ n a m e _ _ )  
  
 B A S E _ U R L   =   ' h t t p s : / / $ s : $ s / a p i / v 1 / n a m e s p a c e s '  
  
  
 c l a s s   O p e n w h i s k _ A P I ( ) :  
         d e f   _ _ i n i t _ _ ( s e l f ,   s e r v e r _ i p = ' 1 2 7 . 0 . 0 . 1 ' ,   s e r v e r _ p o r t = ' 8 4 4 3 ' ,  
                                   b a s e _ u r l = N o n e ,   t i m e o u t = N o n e ,   r a t e _ l i m i t = T r u e ) :  
                 s e l f . O p e n w h i s k _ s e r v e r   =   s e r v e r _ i p  
                 s e l f . O p e n w h i s k _ p o r t   =   s e r v e r _ p o r t  
                 s e l f . _ t i m e o u t   =   6 0 0 0 0       #   6 0 0 0 0   m s e c  
                 s e l f . r a t e _ l i m i t   =   N o n e  
  
                 i f   b a s e _ u r l   i s   N o n e :  
                         s e l f . b a s e _ u r l   =   B A S E _ U R L  
                 e l s e :  
                         s e l f . b a s e _ u r l   =   b a s e _ u r l  
  
                 s e l f . b a s e _ u r l   =   s e l f . b a s e _ u r l   %   ( s e l f . O p e n w h i s k _ s e r v e r ,  
                                                                                   s e l f . O p e n w h i s k _ p o r t )  
  
         d e f   _ R e q u e s t U r l ( s e l f ,   u r l ,   v e r b ,   d a t a = N o n e ,   j s o n = N o n e ) :  
                 " " " R e q u e s t   a   u r l .  
                 A r g s :  
                         u r l :  
                                 T h e   w e b   l o c a t i o n   w e   w a n t   t o   r e t r i e v e .  
                         v e r b :  
                                 E i t h e r   P O S T   o r   G E T .  
                         d a t a :  
                                 A   d i c t   o f   ( s t r ,   u n i c o d e )   k e y / v a l u e   p a i r s .  
                 R e t u r n s :  
                         A   J S O N   o b j e c t .  
                 " " "  
  
                 i f   n o t   d a t a :  
                         d a t a   =   { }  
  
                 i f   v e r b   = =   ' P O S T ' :  
                         i f   d a t a :  
                                 r e s p   =   r e q u e s t s . p o s t ( u r l ,   d a t a = d a t a ,   t i m e o u t = s e l f . _ t i m e o u t )  
                         e l i f   j s o n :  
                                 r e s p   =   r e q u e s t s . p o s t ( u r l ,   j s o n = j s o n ,   t i m e o u t = s e l f . _ t i m e o u t )  
                         e l s e :  
                                 r e s p   =   0     #   P O S T   r e q u e s t ,   b u t   w i t h o u t   d a t a   o r   j s o n  
  
                 e l i f   v e r b   = =   ' G E T ' :  
                         r e s p   =   r e q u e s t s . g e t ( u r l ,   t i m e o u t = s e l f . _ t i m e o u t )  
  
                 e l s e :  
                         r e s p   =   0     #   i f   n o t   a   P O S T   o r   G E T   r e q u e s t  
  
                 i f   u r l   a n d   s e l f . r a t e _ l i m i t :  
                         l i m i t   =   r e s p . h e a d e r s . g e t ( ' x - r a t e - l i m i t - l i m i t ' ,   0 )  
                         r e m a i n i n g   =   r e s p . h e a d e r s . g e t ( ' x - r a t e - l i m i t - r e m a i n i n g ' ,   0 )  
                         r e s e t   =   r e s p . h e a d e r s . g e t ( ' x - r a t e - l i m i t - r e s e t ' ,   0 )  
  
                         s e l f . r a t e _ l i m i t . s e t _ l i m i t ( u r l ,   l i m i t ,   r e m a i n i n g ,   r e s e t )  
  
                 r e t u r n   r e s p  
  
         d e f   s e n d _ t r i g g e r _ e v n e t ( s e l f ,   u r l ,   d a t a ) :  
                 u r l   =   s e l f . b a s e _ u r l   +   u r l  
                 r e s p   =   s e l f . _ R e q u e s t U r l ( u r l ,   v e r b = ' P O S T ' ,   d a t a )  
                 L O G . D E B U G ( " s e n d _ t r i g g e r _ e v e n t   :   % s ,   [ R E S P ]   % s " ,   d a t a ,   r e s p )  
  
  
  
  
  
  
