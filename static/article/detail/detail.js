/*$(function() {
    var navSelector = "#toc-nav";
    var $myNav = $(navSelector);

    $("#article-contents-box").scrollspy({
        target: $("#toc-nav"),
        $nav: $("#toc-nav"),
        $scope: $("#article-contents-box"),
        offset: 10,
    });
})*/

/*
目次を生成する位置にtable-of-contentsをidとして指定
目次を作成する記事が格納されているdivのidをarticle-contents-boxとする
*/

function IndexCreator() {
    function _create() {
        const INDEX = document.getElementById( 'table-of-contents' );
        if ( INDEX === null ) return;

        const CONTENT = document.querySelector( '.content' );
		if ( CONTENT === null ) return;
		
        const HEADING_SELECTORS = '.content > h1, .content > h2, .content > h3, .content > h4, .content > h5, .content > h6';
        const HEADINGS          = CONTENT.querySelectorAll( HEADING_SELECTORS );
        if ( HEADINGS.length === 0 ) return;
      
        _createTitle( INDEX );

        const DIV   = 'div'.createElementAndAddClass( 'items' );
        const ITEMS = _createItems( HEADINGS, DIV );
        INDEX.appendChild( DIV );
        
        const REGISTERER = new IndexEventRegisterer;
        REGISTERER.register( ITEMS, HEADINGS );
    }
  
    function _createTitle( index ) {
        index.insertAdjacentHTML( 'beforeend', '<h3 class="title">目次</h3>' );
    }

    function _createItems( headings, beforeElement ) {
        const getNestCount = function( heading ) {
            let     count       = 1;
            const   NODE_NAME   = heading.nodeName.toLowerCase();

            switch( NODE_NAME ) {
                case 'h2': count = 2; break;
                case 'h3': count = 3; break;
                case 'h4': count = 4; break;
                case 'h5': count = 5; break;
                case 'h6': count = 6; break;
            }

            return count;
        };

        const addNest = function() {
            const OL        = 'ol'.createElement();
            beforeElement   = beforeElement.appendChild( OL );
        };

        const removeNest = function() {
            const OL        = beforeElement.parentNode;
            beforeElement   = OL.parentNode;
        };

        let currentNestCount = 0;

        const adjustNest = function( heading ) {
            const NEST_COUNT = getNestCount( heading );
            if ( currentNestCount === NEST_COUNT ) return false;

            const IS_NEST = currentNestCount < NEST_COUNT;
            
            if ( IS_NEST ) {
                addNest();
            }
            else {
                const REMOVING_COUNT = currentNestCount - NEST_COUNT;
                
                for ( let i = 0; i < REMOVING_COUNT; i++ ) {
                    removeNest();
                }
            }
            
            currentNestCount = NEST_COUNT;

            return IS_NEST;
        };

        let items = [];

        const createItem = function( heading, index ) {
            const IS_NESTED = adjustNest( heading );

            const OL        = IS_NESTED ? beforeElement : beforeElement.parentNode;
            const LI        = 'li'  .createElement();
            const ITEM      = 'div' .createElementAndAddClass( 'item'   );
            const LINE      = 'div' .createElementAndAddClass( 'line'   );
            const NUMBER    = 'div' .createElementAndAddClass( 'number' );
            const TEXT      = 'div' .createElementAndAddClass( 'text'   );
            
            beforeElement = OL.appendChild( LI );
            LI  .appendChild( ITEM      );
            ITEM.appendChild( LINE      );
            LINE.appendChild( NUMBER    );
            LINE.appendChild( TEXT      );

            ITEM.style.paddingLeft  = ( currentNestCount * 10 ) + 'px';
            TEXT.textContent        = heading.textContent;
            
            items.push( ITEM );
        };

        const COUNT = headings.length;
        for ( let i = 0; i < COUNT; i++ ) createItem( headings[i], i );
        
        return items;
    }

    return {
        create: _create,
    }
};

function IndexEventRegisterer() {
    const _SCROLLER = new Scroller( document.documentElement, 70, 15 );

    function _register( items, headings ) {
        const COUNT = headings.length;

        for ( let i = 0; i < COUNT; i++ ) {
            const ITEM      = items[i]; 
            const HEADING   = headings[i];

            _registerHoverEvent ( ITEM, i );
            _registerPushedEvent( ITEM, HEADING );
        }
    }

    function _registerHoverEvent( item, index ) {
        const _CLASS_NAME = 'hover';
        const onStarted   = function() { item.addClass( _CLASS_NAME ); };
        const onEnded     = function() { item.removeClass( _CLASS_NAME ); };

        item.registerOnHover( onStarted, onEnded );
    }

    function _registerPushedEvent( item, heading ) {
        const onPushed = function() { _SCROLLER.scrollByElement( heading ); };

        item.registerOnPushed( onPushed );
    }

    return {
        register: _register,
    };
};

function Scroller( target, speed, interval ) {
    const   _MAX_POSITION   = target.scrollHeight - target.clientHeight;
    let     _timeoutId      = null;

    function _scrollByPosition( position ) {
        if ( _timeoutId !== null ) return;

        let currentPosition = target.scrollTop;
        if ( position > _MAX_POSITION ) position = _MAX_POSITION;
            
        const   DIRECTION   = position < currentPosition ? -1 : 1;
        const   MOVEMENT    = speed * DIRECTION;

        const onScroll = function() {
            currentPosition += MOVEMENT;

            const IS_COMPLETED =
                ( DIRECTION ===  1 && currentPosition >= position ) ||
                ( DIRECTION === -1 && currentPosition <= position )
            ;

            if ( IS_COMPLETED ) {
                target.scrollTop = position;
                _timeoutId = null;

                return;
            }

            target.scrollTop = currentPosition;
            _timeoutId = setTimeout( onScroll, interval );
        };

        onScroll();
    };

    function _scrollByElement( element ) {
        const POSITION = element.offsetTop;

        _scrollByPosition( POSITION );
    }

    return {
        scrollByPosition  : _scrollByPosition,
        scrollByElement   : _scrollByElement,
    };
};

function isSmartPhoneOrTablet() {
    const isContaining = function( search ) {
        return navigator.userAgent.indexOf( search ) !== -1;
    };

    const IS_SMART_PHONE_OR_TABLET = 
        isContaining( 'iPhone' )    || 
        isContaining( 'iPod' )      || 
        isContaining( 'Android' )   ||
        isContaining( 'iPad' )
    ;

    return IS_SMART_PHONE_OR_TABLET;
}

function canUsePassive() {
    let canUsePassive = false;
    
    const PROPERTY  = { get: function() { canUsePassive = true; } };
    const OPTIONS   = Object.defineProperty( {}, 'passive', PROPERTY );

    window.addEventListener( 'dummy', null, OPTIONS );

    return canUsePassive;
}

Element.prototype.registerOnPushed = function( onPushed ) {
    if ( isSmartPhoneOrTablet() ) {
        let     isTouching  = false;
        const   OPTION      = canUsePassive() ? { passive: true } : false;

        const onTouched = function() {
            if ( !isTouching ) return;

            onPushed();
            isTouching = false;
        };

        this.addEventListener( 'touchstart' , function() { isTouching = true;  }, OPTION );
        this.addEventListener( 'touchmove'  , function() { isTouching = false; }, OPTION );
        this.addEventListener( 'touchend'   , onTouched                         , OPTION );
    }
    else {
        this.addEventListener( 'click', onPushed );
    }
};

Element.prototype.registerOnHover = function( onStarted, onEnded ) {
    if ( isSmartPhoneOrTablet() ) {
        const OPTION = canUsePassive() ? { passive: true } : false;

        this.addEventListener( 'touchstart' , onStarted , OPTION );
        this.addEventListener( 'touchend'   , onEnded   , OPTION );
    } 
    else {
        this.addEventListener( 'mouseover'  , onStarted );
        this.addEventListener( 'mouseout'   , onEnded   );
    }
};

String.prototype.createElement = function() {
    return document.createElement( this );
};

String.prototype.createElementAndAddClass = function( className ) {
    const ELEMENT = document.createElement( this );
    ELEMENT.classList.add( className );

    return ELEMENT;
};

Element.prototype.addClass = function( name ) {
    this.classList.add( name );
};

Element.prototype.removeClass = function( name ) {
    this.classList.remove( name );
};

document.addEventListener( 'DOMContentLoaded', function() {
    const INDEX_CREATOR = new IndexCreator;
    INDEX_CREATOR.create();
} );

